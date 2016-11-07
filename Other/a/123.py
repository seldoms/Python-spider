from bs4 import BeautifulSoup
import requests,time
def counter(last=[0]):
    next = last[0] + 1
    last[0] = next
    return next
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.',
    'Cookie':'id58=c5/ns1fuX7txnikxBzEOAg==; bj58_id58s="ajFtS3Z4ditzPTRpODA4MA=="; sessionid=96bb04fb-47c6-480e-a443-5ba82218f599; als=0; bj58_new_session=1; bj58_init_refer="http://bj.58.com/pbdn/0/?PGTID=0d305a36-0000-1663-4d66-147c11f77f4b&ClickID=2"; bj58_new_uv=2; 58tj_uuid=28b95844-f76a-407d-b070-082af9521e58; new_session=1; new_uv=2; utm_source=; spm=; init_refer=http%253A%252F%252Fbj.58.com%252Fpbdn%252F0%252F%253FPGTID%253D0d305a36-0000-1663-4d66-147c11f77f4b%2526ClickID%253D2',
}
urls=['http://bj.58.com/pbdn/0/pn{}/?PGTID=0d305a36-0000-10d4-10a1-543b82161a49&ClickID=2'
          .format(str(i)) for i in range(0,10,1)]
for url in urls:
    url_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(url_data.text,'lxml')
    url_contents = soup.select('td.t > a[onclick]')
    url_lists =[]
    for url_content in url_contents:
        url_content =url_content.get('href')
        url_lists.append(url_content)
    for item in url_lists:
        info_data = requests.get(item,headers =headers)
        info_soup = BeautifulSoup(info_data.text,'lxml')
        categories = list(info_soup.select('#nav > div > span > a'))
        titles = info_soup.select('div.box_left_top > h1')
        prices = info_soup.select('div.price_li > span > i')
        areas = info_soup.select('div.palce_li > span > i')
        views = info_soup.select('p > span.look_time')
        #print(views)
        for category,title,price,area,view in zip(categories,titles,prices,areas,views):
            data ={
                'category':category.get_text(),
                'title':title.get_text(),
                'price':price.get_text(),
                'area':area.get_text(),
                'view':view.get_text(),
            }
            #print(data)
            file_content =data['category']+';;'+data['title']+';;'+data['price']+';;'\
                          +data['area']+';;'+data['view']+'\n'
            with open('d://python/2/58tongcheng_data.txt','a',encoding='utf-8') as file:
                file.write(file_content)
            time.sleep(1)
            print(counter())