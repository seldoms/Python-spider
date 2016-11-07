from bs4 import BeautifulSoup
import requests
import os
import pymongo

client = pymongo.MongoClient('localhost',27017)
baixing = client['baixing']
shouji = baixing['shouji']


def basic_info (url):
    url = 'http://nanjing.baixing.com/shouji/?src=new_home_hot'
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Cookie':'__trackId=147828069559249; __city=nanjing; _gat=1; __sense_session_pv=2; _ga=GA1.2.129125478.1478280697; Hm_lvt_5a727f1b4acc5725516637e03b07d3d2=1478280697; Hm_lpvt_5a727f1b4acc5725516637e03b07d3d2=1478280720; ADEZ_BLOCK_SLOT=FUCKIE; ADEZ_ST=FUCKIE; ADEZ_ASD=1; ADEZ_Source=nanjing.baixing.com/gongzuo/; ADEZ_PVC=1018968-1-iv4jbi18; BDTUJIAID=5cf281b39a86582f92b51944f9fa23b4'
    }
    wb_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(wb_data.text,'lxml')

    titles = soup.select(' div > a.waterfall-title')
    salarys = soup.select('div.waterfall-meta > span.highlight')
    addresss = soup.select('div.waterfall-meta > span.meta-location')
    # print(addresss)
    for title,salary,address in zip(titles,salarys,addresss):
        data = {
            'title': title.get('href'),
            'biaoti':title.get_text(),
            'salary': salary.get_text(),
            'address':address.get_text()

                    # img_soup.find('div', class_ = 'main-image')
        }
        print(data)
        shouji.insert_one(data)


urls = []
for number in range(1, 20):
    urls.append("http://nanjing.baixing.com/shouji/?src=new_home_hot&format=json&page={}".format(number))

# 从链接列表中，用for一个个取出来
for url in urls:
    basic_info(url)