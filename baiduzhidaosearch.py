# -*- coding: utf-8 -*-

import requests
import simplejson
import re
from flask import Flask
from lxml import etree
from headers import Headers
from proxies import Proxies
from urllib import urlencode
from urllib import quote
import chardet

app = Flask(__name__)


@app.route('/baiduzhidaosearch/<keyword>/<page>')
def baiduzhidaosearch(keyword, page):
    ret = {
        'code': 1002,
        'msg': 'failure',
        'data': []
    }
    try:
        page = int(page) * 10
        print 111
        keyword_u = keyword.encode('utf-8')
        print chardet.detect(keyword_u)
        # url = 'http://zhidao.baidu.com/search?word=%s&ie=gbk&site=-1&sites=0&date=0&pn=%s' % (keyword.encode('utf-8 ').decode('gbk','ignore'), page)
        url = u'http://zhidao.baidu.com/search?ct=17&pn=%s&tn=ikaslist&rn=10&word=%s' % (page, keyword)
        #print(url)
        print 222
        headers = Headers.getHeaders()
        proxies = Proxies.get_proxies()
        req = requests.get(url, headers=headers, timeout=60, proxies=proxies)
        if req.status_code == 200:
            ret['code'] = 1001
            ret['msg'] = 'success'
            id = []
            title = []
            req.encoding = 'gbk'
            html = req.text.encode(encoding="utf-8", errors="ignore").decode("utf-8", errors="ignore")
            selector = etree.HTML(html)
            urls = selector.xpath('//div[@class="list"]/dl/dt[1]/a/@href')
            for u in urls:
                match_obj = re.search(r'question/(.*?).html', u, re.M | re.I)
                id.append(match_obj.group(1))
            titles = selector.xpath('//div[@class="list"]/dl/dt[1]/a')
            for t in titles:
                title.append(etree.tostring(t, encoding='utf8', method="html"))
            max_n = len(id)
            n = 0
            while True:
                if n >= max_n:
                    break
                # print(title[n])
                ret['data'].append(
                        {'cid': id[n], 'title': re.search(r'"ti">(.*?)</a>', title[n], re.M | re.I).group(1)})
                n = n + 1
    except Exception as e :
        print e
    return simplejson.dumps(ret)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=3723, use_reloader=True, threaded=True)
