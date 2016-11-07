#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/chart'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER',
    'Cookie':'bid=DytFpIR2E9A; _pk_id.100001.4cf6=86bd9a2094a2dbe9.1476163103.1.1476163103.1476163103.; _pk_ses.100001.4cf6=*; __utmt_douban=1; __utma=30149280.393310073.1476163103.1476163103.1476163103.1; __utmb=30149280.1.10.1476163103; __utmc=30149280; __utmz=30149280.1476163103.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1119547254.1476163103.1476163103.1476163103.1; __utmb=223695111.0.10.1476163103; __utmc=223695111; __utmz=223695111.1476163103.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap=1'
}
wb_data = requests.get(url,headers = header)
soup = BeautifulSoup(wb_data.text,'lxml')

for yp_text in soup.find_all('class="nbg"'):
    yp_texts = yp_text.get('href')
    print(yp_texts)

name = soup.select('div > a')
# print(name)
for zhuyan in soup.find_all('herf'):
    print(zhuyan)


