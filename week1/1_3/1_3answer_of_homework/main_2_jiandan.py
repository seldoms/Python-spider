#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests,urllib.request
from bs4 import BeautifulSoup

url = 'http://jandan.net/ooxx'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

wb_data = requests.get(url,headers = header)
soup = BeautifulSoup(wb_data.text,'lxml')

download_links = []
folder_path = 'D:\dugudown\jiandanMM'
for pic_tag in soup.find_all('img'):
    pic_link = pic_tag.get('src')
    download_links.append(pic_link)

for item in download_links:

    urllib.request.urlretrieve(item,folder_path + item[-10:])

print(soup)