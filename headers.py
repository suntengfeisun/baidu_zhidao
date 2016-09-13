# -*- coding: utf-8 -*-

import platform
import random
from config import Config


class Headers:
    @staticmethod
    def getHeaders():
        if 'Windows' in platform.system():
            headers_path = ''
        else:
            headers_path = Config.headers_path
        userAgentFile = open(headers_path + 'user_agent_list.txt', 'r')
        userAgentList = []
        for line in userAgentFile:
            userAgentList.append({
                'User-Agent': line.strip(),
                #'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html) ',
                'Referer': Config.headers_referer,
                'X-Forwarded-For': '%s.%s.%s.%s' % (
                random.randint(50, 250), random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)),
                'CLIENT-IP': '%s.%s.%s.%s' % (
                random.randint(50, 250), random.randint(50, 250), random.randint(50, 250), random.randint(50, 250))
            })
        userAgentFile.close()
        userAgent = random.sample(userAgentList, 1)
        return userAgent[0]
