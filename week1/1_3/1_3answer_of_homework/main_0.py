#!/usr/bin/env python
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = 'http://sh.xiaozhu.com/fangzi/2303611027.html'
headers = {
  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
  'Cookie':'abtest_ABTest4SearchDate=b; OZ_1U_2282=vid=v7f3c69fed80eb.0&ctime=1475593887&ltime=0; OZ_1Y_2282=erefer=-&eurl=http%3A//gz.xiaozhu.com/fangzi/2303611027.html&etime=1475593887&ctime=1475593887&ltime=0&compid=2282; _ga=GA1.2.1488476801.1475593889; gr_user_id=13bbe192-e386-4074-8ca0-a4a882ba66aa; gr_session_id_59a81cc7d8c04307ba183d331c373ef6=8d7a3db1-e35f-4f23-9ce3-e73afd78b45a; __utma=29082403.1488476801.1475593889.1475594056.1475594056.1; __utmb=29082403.1.10.1475594056; __utmc=29082403; __utmz=29082403.1475594056.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'

}
def get_lorder_sex(class_name):
        if class_name == ['member_ico1']:
                return '女'
        else:
                return '男'

def get_links(url):
    wb_data = requests.get(url,'headers')
    soup = BeautifulSoup(wb_data.text,'lxml')

    titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    # 获取标题
    addresss = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
    # 获取地址
    moneys = soup.select('#pricePart > div.day_l > span')
    # 获取价格
    imgs = soup.select('#curBigImage')
    # 获取大图
    littleimgs = soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > a > img")
    # 获取房东头像
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    # 获取房东姓名
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')
    # 判断房东性别

    for title,address,money,img,littleimg,name,sex in zip (titles,addresss,moneys,imgs,littleimgs,names,sexs):
        data = {
                'title':title.get_text(),
                'address':address.get_text(),
                'money':money.get_text(),
                'img':img.get('src'),
                'sex':get_loder_sex(sex.get("class"))
        }
        print(data)
# 生成10个列表页面地址
urls = []
for number in range(1, 10):
    urls.append("http://bj.xiaozhu.com/search-duanzufang-p{}-0/".format(number))

# 从链接列表中，用for一个个取出来
for single_url in urls:
    # 把得到的列表页面链接，传给函数，这个函数可以得到详情页链接
    get_links(single_url)
