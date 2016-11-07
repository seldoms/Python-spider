#coding:utf-8
from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
doubanTOP250 = client['doubanTOP250']
movie = doubanTOP250['movie']

header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
'Cookie':'bid=DytFpIR2E9A; ap=1; _pk_id.100001.4cf6=86bd9a2094a2dbe9.1476163103.4.1477807410.1476208248.; _pk_ses.100001.4cf6=*; __utmt_douban=1; __utma=30149280.393310073.1476163103.1476208248.1477807410.4; __utmb=30149280.1.10.1477807410; __utmc=30149280; __utmz=30149280.1476163103.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1119547254.1476163103.1476208249.1477807410.4; __utmb=223695111.0.10.1477807410; __utmc=223695111; __utmz=223695111.1476163103.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
}

def basic_info (url):
    wb_data = requests.get(url,headers = header)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,"lxml")

    tops = soup.select(' div > div.article > ol > li > div > div.pic > em')
    titles = soup.select('div > div.article > ol > li > div > div.info > div.hd > a ')
    pics = soup.select('div > div.article > ol > li > div > div.pic > a > img')
    stars = soup.select(' div > div.article > ol > li > div > div.info > div.bd > div > span.rating_num')
    comments = soup.select(' div > div.article > ol > li > div > div.info > div.bd > p.quote > span')
    # print(titles)
    for top,title,pic,star,comment in zip (tops,titles,pics,stars,comments):
        data = {
            'top'  :top.get_text(),
            'title': title.get_text(),
            'pic'  :pic.get('src'),
            'star' :star.get_text(),
            'comment':comment.get_text()

        }
        # print(data)
        movie.insert_one(data)

def find_stars():
    # 从qiubai数据库的likej表，查询所有数据，用find()函数
    for info in movie.find():
        # info 我们插入的数据都有title和like，我们取出每条信息的like，用来比较
        if info[int('star')] >= '9':
            print (info)
find_stars()

urls = []
for number in range(25,250,25):
    urls.append("https://movie.douban.com/top250?start={}&filter=".format(number))

# 从链接列表中，用for一个个取出来
for single_url in urls:
# 把得到的列表页面链接，传给函数，这个函数可以得到详情页链接
    basic_info(single_url)



