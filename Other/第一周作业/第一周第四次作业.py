import  requests
from bs4 import BeautifulSoup
import urllib.request
import time

path="C:\\Users\\admin\\Desktop\\taile\\"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
    "Cookie":'locale=zh-cn; __whiAnonymousID=a92a3644e4344a0d9870ad03a642f564; __qca=P0-1773715510-1474905445536; _weheartit_anonymous_session=%7B%22page_views%22%3A1%2C%22search_count%22%3A0%2C%22last_searches%22%3A%5B%5D%2C%22last_page_view_at%22%3A1474986416351%7D; __gads=ID=3a5e327d901f66e2:T=1474986510:S=ALNI_MZqNdlgT6eNKlN9xAD8z8nNparkNQ; __utmt=1; __utma=222371101.4807005.1474905448.1474986416.1474986416.2; __utmb=222371101.3.10.1474986416; __utmc=222371101; __utmz=222371101.1474986416.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=222371101.|27=locale=zh-cn=1; auth=no; _session=2fac7e2ece6f7c964d44617be7ed612e; _ga=GA1.2.4807005.1474905448'

}
urls = ["http://weheartit.com/inspirations/taylorswift?page={}".format(str(a)) for a in range(1, 15)]
data = []
for url in urls:

    wb_data = requests.get(url, headers=headers)
    time.sleep(2)

    soup = BeautifulSoup(wb_data.text, "lxml")
    imgs = soup.select('img.entry-thumbnail')
    print(imgs)

    for img in (imgs):
        data.append(img.get('src'))





#print(data)
for i in data:
    urllib.request.urlretrieve(i, path+i.split("/")[-2]+i.split("/")[-1])
    print("done")










