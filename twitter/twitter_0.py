# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://twitter.com/catLin0/media'
# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
# 'Cookie':'guest_id=v1%3A147585410569147028; kdt=3sOEJfQnl3zc1cGsAgue0uafJZKOhLU7uF0qtc0y; remember_checked_on=1; twid="u=346382831"; auth_token=6faa99fdedd3aa7c290f8adcef9545307a36bb09; lang=zh-cn; _ga=GA1.2.1360072780.1475854110; _gat=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCMcNH6ZXAToMY3NyZl9p%250AZCIlZmVmZGI2MTU5YjE2MTc4ODQ5NWQxZWFjY2MwMDIzM2Y6B2lkIiVhZDg3%250AZWJlYzU0NTc0ZmQ2NTMyODcwZmY3ODZjMDZlMQ%253D%253D--3052932ccb7f17274b35fc88311437d503bec9a4'}
#
# wb_data = requests.get(url, 'headers')
# soup = BeautifulSoup(wb_data.text, 'lxml')
#
# print(soup)

__author__ = 'Liutao'
# -*- coding:utf-8 -*-
import urllib
import urllib.request
# import urllib2
import re
from bs4 import BeautifulSoup
import os

url = "http://www.bullbill.com/news/264a1404.html"

html = urllib.request.urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")
imgPPTList = bsObj.findAll("img", {"alt": "私募基金协会最新培训材料（144页PPT，私募必读）"})
length = len(imgPPTList)
path = os.getcwd()  # 获取此脚本所在目录
new_path = os.path.join(path, 'abc')#在当前脚本所在目录新建名为abc的文件夹
if not os.path.isdir(new_path):
    os.mkdir(new_path)
for i in range(length):
    # print(imgPPTList[i].attrs["src"])
    print(imgPPTList[i].get("src"))
    urllib.request.urlretrieve(imgPPTList[i].attrs["src"], os.path.join(new_path, str(i) + ".jpg"))
    print(str(i) + ".jpg,下载成功！")