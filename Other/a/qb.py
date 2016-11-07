from bs4 import BeautifulSoup
import requests
import urllib.request
import urllib
import urllib.parse
import os


header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Cookie':'_qqq_uuid_="2|1:0|10:1476162679|10:_qqq_uuid_|56:ODkwMDIxMGIwOWNhZTZkNWNhNTg0YmIxMmJiMTIzNTZiYWQyNWJkMw==|d70c08f846415db419f4fd24cd41ff96f08afe34355b15621d1f468b1f03c82f"; _qqq_auth_token=3376e70fdb5f395a3610392650d27f2604e03f55; __cur_art_index=2000; _xsrf=2|6aac40c5|5676735538721021e3e8f9a8a60cb66e|1476435981; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1476162681,1476435982; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1476435982; _qqq_user_id=3265869; _qqq_user="c2VsZG9tcw=="; _ga=GA1.2.1284580068.1476162681; _gat=1'
}

url = 'http://www.qiushibaike.com/'
def judgment_gender(class_name):
    if 'womenIcon' in class_name :
        return '女'
    else:
        return '男'
# def get_lorder_sex(class_name):
#     if class_name == ['member_boy_ico']:
#         return '男'
#     else:
#         return '女'
# def get_detail_info(url):

# 这个是刚才的错误
# name 'judgment_gender' is not defined，报错提示，函数没定于
# 解决方法，定义函数，再次运行
# name 'sex' is not defined，sex没定义
# 用gender替代sex，再次运行
# name 'class_name' is not defined，提示class_name没定义，找到并发现没有class_name，用函数得到的参数替代
# 再次运行，ok
# http://pic.qiushibaike.com/system/avtnew/1146/11460623/medium/20140816125723.jpg
# def download(url):
#     r = requests.get(url, headers=headers)
#     if r.status_code != 200:
#         return
#
#     filename = url.split("/")[-2]
#
#     target = "./{}.jpg".format(filename)
#
#     with open(target, "wb") as fs:
#         fs.write(r.content)
#
#     print("%s => %s" % (url, target))



def get_detail_info(url):
    wb_data = requests.get(url,headers = header)
    soup = BeautifulSoup(wb_data.text,'lxml')
    # print(soup)
    names = soup.select('div.author.clearfix > a > h2')
    titles = soup.select(' a.contentHerf > div')#a.contentHerf > div
    imgs = soup.select('div.author.clearfix > a > img')
    funs = soup.select('div.stats > span.stats-vote > i')
    genders = soup.select('div.author.clearfix > div')
    ages = soup.select('div.author.clearfix > div')
    # print(imgs)
    # for title,img,like,fun,gender in zip(titles,imgs,likes,funs,genders):
    for title,img,fun,gender,name,age in zip(titles,imgs,funs,genders,names,ages):
        data = {
            # 'gender': gender.get('class'),
            'gender': judgment_gender(gender.get('class')),
            'age'    :age.get_text(),
            'title' :title.get_text(),
            'img'   : img.get('src'),
            'fun'   : fun.get_text(),
            'name'  :name.get_text()
            #如何查看提取出来单个的内容
        }
        print(data)
        # open(path, 'w')：w
    # file = open('D://S/1.txt', 'w')
    # file.write(str(titles))
    # file.close()


urls = []
for number in range(1, 35):
    urls.append("http://www.qiushibaike.com/8hr/page/{}/?s=4921516".format(number))

# 从链接列表中，用for一个个取出来
for single_url in urls:
# 把得到的列表页面链接，传给函数，这个函数可以得到详情页链接
    get_detail_info(single_url)






'''
#qiushi_tag_117745952 > div.stats > span.stats-vote > i
#qiushi_tag_117745642 > div.stats > span.stats-vote > i
#qiushi_tag_117745695 > a.contentHerf > div
#qiushi_tag_117745737 > a.contentHerf > div > span
#qiushi_tag_117745643 > a.contentHerf > div > span
//*[@id="qiushi_tag_117745643"]/a[1]/div/span
#qiushi_tag_117746562 > a.contentHerf > div
#qiushi_tag_117745737 > div.author.clearfix > a:nth-child(1) > img
#qiushi_tag_117745643 > div.author.clearfix > a:nth-child(1) > img
#qiushi_tag_117745952 > div.stats > span.stats-vote > i
#qiushi_tag_117745952 > div.author.clearfix > div

'''