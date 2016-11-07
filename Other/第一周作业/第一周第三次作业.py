from bs4 import BeautifulSoup
import requests
import time
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    'Cookie':'abtest_ABTest4SearchDate=b; xzuuid=28e6987b; _gat_UA-33763849-7=1; gr_user_id=9369ac48-2298-4d2e-b61e-0791ff671f54; __utmt=1; OZ_1U_2282=vid=v7e49c97a80386.0&ctime=1474600531&ltime=1474600109; OZ_1Y_2282=erefer=-&eurl=http%3A//bj.xiaozhu.com/search-duanzufang-p1-0/&etime=1474600087&ctime=1474600531&ltime=1474600109&compid=2282; _ga=GA1.2.1016582563.1474600088; gr_session_id_59a81cc7d8c04307ba183d331c373ef6=f6ee11b1-e58e-452c-a57e-8d1a7bdb78bc; __utma=29082403.1016582563.1474600088.1474600088.1474600088.1; __utmb=29082403.3.10.1474600088; __utmc=29082403; __utmz=29082403.1474600088.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
}

'''url_saves = 'http://bj.xiaozhu.com/fangzi/1142158065.html'
wb_data = requests.get(url_saves, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
titles = soup.select("div.pho_info > h4")
addresses = soup.select('span.pr5')
prices = soup.select('div.day_l')
images = soup.select('img#curBigImage')
host_names = soup.select('a.lorder_name')
host_pic = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
host_gendars = soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > div")'''

#print(titles)


'''def print_gendar(css_name):

    if css_name == 'member_ico1':
        return "female"
    if css_name == 'member_ico':
        return "male"'''
def print_gender(class_name):
    if class_name == ['member_ico1']:
        return '女'
    if class_name == ['member_ico']:
        return '男'



'''for title, address, price, image, host_name, host_img, host_gendar in zip(titles, addresses, prices, images,host_names, host_pic, host_gendars):
    data = {
        'title': title.get_text(),
        'address': address.get_text(),
        'price': price.get_text(),
        'image': image.get('src'),
        'host_name': host_name.get_text(),
        'host_img': host_img.get("src"),
        'host_gendar': print_gender(host_gendar.get('class'))

    }
    print(data)'''


urls=["http://bj.xiaozhu.com/search-duanzufang-p{}-0/".format(str(i)) for i in range(1, 13, 1)]
#print(urls)

def get_data(url):

    wb_data = requests.get(url,headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select("div.pho_info > h4")
    addresses = soup.select('span.pr5')
    prices = soup.select('div.day_l')
    images = soup.select('img#curBigImage')
    host_names = soup.select('a.lorder_name')
    host_pic = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    host_gendars = soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > div")

    for title, address, price, image, host_name, host_img, host_gendar in zip(titles, addresses, prices, images,
                                                                              host_names, host_pic, host_gendars):
        data = {
            'title': title.get_text(),
            'address': address.get_text(),
            'price': price.get_text(),
            'image': image.get('src'),
            'host_name': host_name.get_text(),
            'host_img': host_img.get("src"),
            'host_gendar': print_gender(host_gendar.get('class'))

        }
        print(data)

for single_url in urls:


    ww_data = requests.get(single_url,headers=headers)
    soup = BeautifulSoup(ww_data.text, "lxml")
    detail_urls = soup.select('a[class="resule_img_a"]')
    for detail_url in detail_urls:
        house_data = detail_url.get('href')
        get_data(house_data)
















