# -*- coding: utf-8 -*-

import requests
import simplejson
import re
from flask import Flask
from lxml import etree
from headers import Headers
from proxies import Proxies

# aaa= 'http://zhidao.baidu.com/question/424987546428383692.html?fr=iks&word=333&ie=gbk'
# match_obj = re.match(r'n/(.*?).h', aaa, re.M | re.I)
# print(match_obj)


line = "http://zhidao.baidu.com/question/424987546428383692.html?fr=iks&word=333&ie=gbk"

matchObj = re.search( r'question/(.*?).html', line, re.M|re.I)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"