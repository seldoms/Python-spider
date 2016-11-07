from bs4 import BeautifulSoup
import requests
import os

url = 'http://www.mzitu.com/all'
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
'Cookie':'Hm_lvt_94a3ec366028363d5c3adac4b1df34e4=1477907826; Hm_lpvt_94a3ec366028363d5c3adac4b1df34e4=1477908701'
}

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

lists = soup.find('div',class_='all').find_all('a')
for a in lists:
    title= a.get_text(),#提取妹子详情页的标题，作文件夹名用
    herf  = a['href']#提取所有妹子的详情页主页
    # print(title)

    pic_url = requests.get(herf)
    pic_info = BeautifulSoup(pic_url.text,'lxml')
    # print(pic_url)









'''
body > div.main > div.main-content > div.all > ul:nth-child(3) > li:nth-child(3) > p.url.on > a:nth-child(5)
body > div.main > div.main-content > div.all > ul:nth-child(3) > li:nth-child(3) > p.url.on


'''