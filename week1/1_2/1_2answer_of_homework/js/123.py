from bs4 import BeautifulSoup
with open('C:/Users/seldo/Documents/Plan-for-combating-master/week1/1_2/1_2answer_of_homework/index.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    titles = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right")
    reviews = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right")
    prices = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right")
    stars = Soup.select("div > div.ratings > p:nth-of-type(2)")###这里对于star元素的处理，是怎么知道截取这一段代码才能筛选出所需内容的？
    #-star--body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(2) > div > div.ratings > p:nth-child(2)
    print(len(titles), len(images), len(reviews), len(prices), len(stars))
for image,title,review,price,star in zip (images,titles,reviews,prices,stars):
    title_content = title.get_text()
    review_content = review.get_text()
    price_content = price.get_text()
    image_content = image.get("src")
    star_content = len(star.find_all("span", "glyphicon glyphicon-star"))
    # title_content = title.get_text()
    # image_content = image.get("src") #--image标签用get，不是get——text
    # review_content = review.get_text()
    # price_content = price.get_text()
    # star_content = star.get_text()

    data = {
        "titles" : title_content,
        "imags" : image_content,
        "reviews" : review_content,
        "prices" : price_content,
        "stars" : star_content
    }
    print(data)
