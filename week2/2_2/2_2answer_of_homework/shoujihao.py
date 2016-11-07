import requests
from bs4 import BeautifulSoup
import pymongo
import re


urls = []
for number in range (1,71):
    urls.append('http://nj.58.com/shoujihao/pn{}/'.format(number))
    # 从链接列表中，用for一个个取出来
for single_url in urls:
    # 把得到的列表页面链接，传给函数，这个函数可以得到详情页链接
    get_detail_info = (single_url)
    print(get_detail_info)

def title_url(single_url):
    wb_data = requests.get(get_detail_info)
    soup = BeautifulSoup(wb_data.text,('lxml'))
    titles = soup.select('#infolist > div > ul > div > ul > li > a.t')
    numbers = soup.select('#infolist > div > ul > div > ul > li > a.t > strong')
    for title,number in zip(titles,numbers):
        data ={
            'title' : title.get_text(),
            'number': number.get('herf')
        }
        print(data)

title_url(get_detail_info)



