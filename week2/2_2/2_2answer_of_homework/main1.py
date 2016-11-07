import requests
from bs4 import BeautifulSoup
import pymongo
import time


client = pymongo.MongoClient('localhost',27017)

qiubai = client['qiubai']

likej = qiubai['likej']

title = qiubai['title']


# spider1
def get_links_from(page):
    # 根据列表页面链接规律，拼接列表页面地址
    url = 'http://www.qiushibaike.com/textnew/page/{}/'.format(page)
# 请求列表页面地址
    wb_data = requests.get(url)

# 延时一秒钟，太快容易被封IP
    time.sleep(1)

# 开始解析网页数据
    soup = BeautifulSoup(wb_data.text, 'lxml')

    titles = soup.select(' a.contentHerf > div')

    # 提取Css Path
    likes = soup.select('div.stats > span.stats-vote > i')

    # 由于soup.select得到的是列表，需要用for一个个遍历出来
    for title, like in zip(titles, likes):
        data = {
            'title': title.get_text(),
            'like': like.get_text()
        }

        # print(data)
        likej.insert_one(data)
        # title.insert_one(title)
def find_likes():
    # 从qiubai数据库的likej表，查询所有数据，用find()函数
    for info in likej.find():
        # info 我们插入的数据都有title和like，我们取出每条信息的like，用来比较
        if info[str('like')] >= '300':
            print (likej)

for page in range(1, 2):
    get_links_from(page)

find_likes()


# for info in likej.find():
# 	url = info["url"]

