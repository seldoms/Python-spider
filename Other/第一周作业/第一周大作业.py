from bs4 import BeautifulSoup
import  requests
import time
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.',
    'Cookie':'id58=c5/ns1fuX7txnikxBzEOAg==; bj58_id58s="ajFtS3Z4ditzPTRpODA4MA=="; sessionid=96bb04fb-47c6-480e-a443-5ba82218f599; als=0; bj58_new_session=1; bj58_init_refer="http://bj.58.com/pbdn/0/?PGTID=0d305a36-0000-1663-4d66-147c11f77f4b&ClickID=2"; bj58_new_uv=2; 58tj_uuid=28b95844-f76a-407d-b070-082af9521e58; new_session=1; new_uv=2; utm_source=; spm=; init_refer=http%253A%252F%252Fbj.58.com%252Fpbdn%252F0%252F%253FPGTID%253D0d305a36-0000-1663-4d66-147c11f77f4b%2526ClickID%253D2',
}


urls=['http://bj.58.com/pbdn/0/pn{}/?PGTID=0d305a36-0000-1467-426b-f2ae60490864&ClickID=7'.format(str(i)) for i in range (0,11,1)]
data = []  # 将页面中所有商品的链接放在data中
for url in urls:
    we_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(we_data.text, "lxml")
    # print(soup)
    links = soup.select("#infolist > div.infocon > table > tbody > tr > td.t > a")
    # print(links)

    for link in links:
        cd = link.get("href")
        data.append(cd)


#print(data  )



def ab (url):
    good_data = requests.get(url, headers=headers)
    time.sleep(3)
    soup = BeautifulSoup(good_data.text, 'lxml')
    # print(soup)
    categorys = str(soup.select("#nav > div > span > a")[-1])
    titles = soup.select("h1.info_titile")
    prices = soup.select(
        "body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.price_li > span > i")
    areas = soup.select(
        "body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span > i")
    views = soup.select(
        "body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > p > span.look_time")

    for  title, price, area, view in zip(titles, prices, areas, views):
        all_data = {
            "category": categorys[-10:-4],

            'title': title.get_text(),
            "price": price.get_text(),

            'area': area.get_text(),
            'view': view.get_text(),

        }
        print(all_data)


for i in data:
    ab(i)











