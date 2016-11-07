from bs4 import BeautifulSoup
import requests
import urllib.request

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Cookie':'_qqq_uuid_="2|1:0|10:1476162679|10:_qqq_uuid_|56:ODkwMDIxMGIwOWNhZTZkNWNhNTg0YmIxMmJiMTIzNTZiYWQyNWJkMw==|d70c08f846415db419f4fd24cd41ff96f08afe34355b15621d1f468b1f03c82f"; _qqq_auth_token=3376e70fdb5f395a3610392650d27f2604e03f55; __cur_art_index=2000; _xsrf=2|6aac40c5|5676735538721021e3e8f9a8a60cb66e|1476435981; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1476162681,1476435982; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1476435982; _qqq_user_id=3265869; _qqq_user="c2VsZG9tcw=="; _ga=GA1.2.1284580068.1476162681; _gat=1'
}
# url = 'http://www.qiushibaike.com/pic/page/{}/?s=4922656'.format(1,35)
for page in range(1, 35):
    # 找规律，发现只有替换请求链接的page参数即可进入相应页面
    url = 'http://www.lameshuang.com/meinv/japan/'
#获取网页信息并解析
    wb_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    # print(soup)
#将清洗过后的图片链接放进列表内
    download_links = []
#指定下载文件夹路径供循环调用
    folder_path = 'd://abc/'
#清洗获取到的图片链接
    for pic in soup.select(' div > a > img'):
            pic_link = pic.find_all('width="236"')
            download_links.append(pic_link)
            print(pic_link)
        #下载循环，成功一个输出“done”
    # for item in download_links:
    #         urllib.request.urlretrieve(item,folder_path + item[-10:])
    #         print('Done')





# def download(pic_link)

