import requests
from bs4 import BeautifulSoup
import pymongo



client = pymongo.MongoClient('locallhost',27017)
xiaozhu = client['xiaozhu']
fangzi = xiaozhu['fangzi']


header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

def insert_fangzi_info(url):
    pass

def faind_fangzi():
    pass



# for page in range(1,4):
#     url = 'http://nj.xiaozhu.com/search-duanzufang-p{}-0/'.format(page)
#     wb_data = requests.get(url,headers = header)
#     soup = BeautifulSoup(wb_data.text,'lxml')
#     price = soup.select('span.result_price > i')
#     address = soup.select('div.result_btm_con.lodgeunitname > div > a > span')
#     print(price,address)

find_fangzi()

