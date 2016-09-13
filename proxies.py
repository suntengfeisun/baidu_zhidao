# -*- coding: utf-8 -*-

from random import choice

class Proxies:
    @staticmethod
    def get_proxies():
        proxies = [
            # {"http": "http://47.88.1.153:8088", "https": "https://47.88.22.153:8088"},
            {"http": "http://112.124.50.167:8088", "https": "https://112.124.50.167:8088"},
            # {"http": "http://45.79.172.201:8088", "https": "https://45.79.72.201:8088"},
            {"http": "http://47.88.12.208:8088", "https": "https://47.88.12.208:8088"},
            # {"http": "http://47.88.22.173:8088", "https": "https://47.88.22.173:8088"}
        ]
        return choice(proxies)
