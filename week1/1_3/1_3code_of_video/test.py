from bs4 import BeautifulSoup
import requests
import lxml
import time

url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
headers = {'User-Agent':'Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53',
'Cookie':'TAUnique=%1%enc%3A2YLmNxB4JhxBipNjkBt5DrYrsTgATOWX8ahZNDPHfDsYvJ58lDKZ6g%3D%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TASSK=enc%3AAOVVsTd9ka4jgNz2t47RagKkGAQoNdFb0pia%2BrvtsjzDaSrL5DjMmqkMPPFuKF6yloJKrxvEo%2F91mpjDj5DBX%2Bce81YCMCQji1TPVxEucWh%2BGWyUiIW5%2BsnKJgNpc1UelQ%3D%3D; TAPD=tripadvisor.cn; CommercePopunder=SuppressAll*1475471962132; TAAuth2=%1%3%3A57f5348796fd30704c3358f95896a21a%3AAI6zwRTAKN9oRgMaAZjbW5M3shbUog4PlDKpqX326UyxVURAd5aZcPEP4IIIUsnPfZDH9FOExhhbN0sm9RfrVapCRjDm1v8UpoOoStZCXpjOMfFPHB4uVZjOkJMEuGq65Om9CarTzdWGWKx7lj2rqHy4ZIwkbokJID9ImIvfDne%2B1cO7hjnIuYLOzIsfOw6XvHO25Qk%2F0aa5xr2Nsst9W4Y%3D; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1475429297; ki_t=1475429297656%3B1475429297656%3B1475472011378%3B1%3B2; ki_r=; ServerPool=C; CM=%1%HanaPersist%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CFtrSess%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Csh%2C%2C-1%7C2016sticksess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCPers%2C%2C-1%7CCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7Csesssticker%2C%2C-1%7C2016stickpers%2C%2C-1%7Ct4b-sc%2C%2C-1%7CViatorMCSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C1%2C-1%7Cperscoestorem%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; roybatty=TNI1625!AFvH7hCYRWcNOs%2Bl0SLT2Xv%2B7mLuPmnIEiC8qe5oIKe3gHDx5oHzCU2MSrpL8dlhi9iZH7KU7xodiwg4CiP6GODjzTWzVu8vTtfuxFnXP1wV0Ha4ixchwfDgt4bo5S6R8ijqO6J7seyuCjTTOEjiQg1qozNhGd7%2Bkdt8YXFvCI%2Fm%2C1; TASession=%1%V2ID.F0E4983AF3873403D9121806942794DA*SQ.2*LS.PageNotFound*GR.35*TCPAR.15*TBR.91*EXEX.65*ABTR.66*PPRP.76*PHTB.4*FS.86*CPU.91*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.191980FAA7109EABB109B38FA8E9BFC5*FA.1*DF.0*LP.%2FAttractions-g60763-Activities-New_York_City_New_York%5C.html*FLO.60763*TRA.true*LD.60763; TAUD=LA-1475489124099-1*LG-1-2.1.F.*LD-2-.....'

          }

# wb_data = requests.get(url)
#     # time.sleep(4)
#     soup = BeautifulSoup(wb_data.text,'lxml')
#     print(soup)
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('div.property_title')
    print(soup)


