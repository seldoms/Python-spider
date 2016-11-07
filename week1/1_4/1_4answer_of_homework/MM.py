#!/usr/bin/env python
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://www.tutu12345.net/a/cn/xiuren/2016/1011/22015.html/'
header = {
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0','Host':'www.tutu12345.net',
'If-Modified-Since':'Wed, 12 Oct 2016 07:40:30 GMT',
'If-None-Match':'"eacb26e85b24d21:12e8"',
'Referer':'http://www.tutu12345.net/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
wb_data = requests.get(url,headers = header)
soup = BeautifulSoup(wb_data.text,'lxml')
print(soup)

imgs = soup.select('body > div.page-list > p > img')
print(imgs)
