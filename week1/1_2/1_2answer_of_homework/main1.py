from bs4 import BeautifulSoup
with open('C:/Users/seldo/Documents/Plan-for-combating-master/week1/1_2/1_2answer_of_homework/index.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    # images = Soup.select('/html/body/div[1]/div/div[2]/div[2]/div[1]/div/img')
    print(Soup.find_all(title))
    # '''
    # body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > img
    #
    # '''