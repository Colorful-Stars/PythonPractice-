#!/usr/bin/env python
# -*- coding = utf-8 -*-

import requests
def getHtmlText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(getHtmlText(url))