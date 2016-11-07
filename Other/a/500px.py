import requests
from bs4 import BeautifulSoup


url = 'https://500px.com/popular'
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Cookie':'landing_page=%2Fphoto%2F79870757%2Fnovice-monks-by-oscar-tarneberg; referrer_type=other; location=CN; optimizelyEndUserId=oeu1476994809736r0.6215503603608845; optimizelySegments=%7B%22569090246%22%3A%22false%22%2C%22569491641%22%3A%22referral%22%2C%22575800731%22%3A%22gc%22%2C%22589900200%22%3A%22true%22%7D; optimizelyBuckets=%7B%7D; _hpx1=BAh7CkkiD3Nlc3Npb25faWQGOgZFVEkiJWNlNmUyN2YyNDI4ZWNkNGQ4MGQyZGZhOWZhY2M3ZjJkBjsAVEkiCWhvc3QGOwBGIhJhcGkuNTAwcHguY29tSSIYc3VwZXJfc2VjcmV0X3BpeDNscwY7AEZGSSIQX2NzcmZfdG9rZW4GOwBGSSIxVUQ4TlZzQ2kvQnJBWkNMZXBLbFJJbkR5c0VKZlpPTTA1OHZSZ0RhTitTaz0GOwBGSSIRcHJldmlvdXNfdXJsBjsARkkiDS9wb3B1bGFyBjsAVA%3D%3D--78bc4a362e8133e146d0470831582acb3317c2f4; photo_download_expanded=true; user_license_selection=print_ready; photo_details_expanded=false; _ga=GA1.2.1895779090.1476994810; amplitude_id500px.com=eyJkZXZpY2VJZCI6ImEyMzY0ZmJjLTFiYTEtNGI1ZC05MGZlLTZkNDEyMDgwN2I5M1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTQ3Njk5NDgxMDQyNiwibGFzdEV2ZW50VGltZSI6MTQ3Njk5NTExMjEzNSwiZXZlbnRJZCI6MiwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjJ9'
}
wb_data = requests.get(url,headers = header)
soup = BeautifulSoup(wb_data.text,'lxml')
pic_link = soup.select('')
print(pic_link)