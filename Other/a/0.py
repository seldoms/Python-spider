from bs4 import BeautifulSoup
import requests,urllib.request
#proxy ={"http": "hk.a.cloudss.pw:31929"}
def counter(last=[0]):
    next = last[0] + 1
    last[0] = next
    return next
header ={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    'Cookie':'locale=zh-cn; __whiAnonymousID=6cb6dab9af224bdfbfe9ba1f04ebc152; __qca=P0-1178749198-1474707009141; _weheartit_anonymous_session=%7B%22page_views%22%3A3%2C%22search_count%22%3A0%2C%22last_searches%22%3A%5B%5D%2C%22last_page_view_at%22%3A1474768141514%7D; __utmt=1; auth=no; _session=6d81e59c2b3e7a52ea34b397e4640ec3; __utma=222371101.1562661476.1474707010.1474719264.1474768144.2; __utmb=222371101.2.10.1474768144; __utmc=222371101; __utmz=222371101.1474719264.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=222371101.|27=locale=zh-cn=1; _ga=GA1.2.1562661476.1474707010'
    }
#urls = 'http://weheartit.com/inspirations/taylorswift?scrolling=true&page={}&before=259965971'\
    #.format((str(i)) for i in range(0,10,1))
#for url in urls:
#url ='http://weheartit.com/inspirations/taylorswift?scrolling=true&page=2&before=259965971'
#def get_imgs(url):
urls = ['http://weheartit.com/inspirations/taylorswift?scrolling=true&page={}&before=259965971'.format(str(i)) for i in range(1,11)]
for url in urls:
    wb_data= requests.get(url,headers=header)
    soup = BeautifulSoup(wb_data.text,'lxml')
    imgs = soup.select('div > a > img[class="entry-thumbnail"]')
    list = []
    for img in imgs:
        img = img.get('src')
        list.append(img)
    #print(list,sep='\n')
    path ='d://python/2/'
    for item in list:
        img_name = item[-24:].replace('/''superthumb','')
        #print(img_name)
        urllib.request.urlretrieve(item,path+img_name)
        print(counter())
        #print(item)
    #print(imgs)

