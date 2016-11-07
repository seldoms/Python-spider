#coding:utf-8
#--------------------------------------------------
#   程序：获取豆瓣top250电影
#   作者：lazyboy
#   博客：http://blog.lazyboy.co/
#   日期：2014-12-20
#   语言：Python 2.7
#--------------------------------------------------
import requests,re
# 初始链接
url = 'http://movie.douban.com/top250'
# 函数，获得电影链接和标题
def getlists(u):
    links = []
    titles = []
    r = requests.get(u)
    if r.status_code == 200:
        t = r.content
        p = re.compile('(?<=<ol\sclass="grid_view">)(.|\n)+?(?=</ol>)')
        m = p.search(t)
        if m:
            alllists = m.group()
            p2 = re.compile('(?<=</li>)\n.+?(?=<li>)')
            m2 = p2.split(alllists)
            p3 = re.compile('(?<=href=").+?(?=")')
            p4 = re.compile('(?<=class="title">).+?(?=</span>)')
            for i in range(0,len(m2)):
                m3 = p3.search(m2[i])
                m4 = p4.search(m2[i])
                if m3 and m4:
                    links.append(m3.group())
                    titles.append(m4.group())
            return (links,titles)
# 函数，获得下一页网页链接
def nexturl(u):
    r = requests.get(u)
    if r.status_code == 200:
        t = r.content
        p = re.compile('(?<=rel="next"\shref=").+?(?=")')
        m = p.search(t)
        if m:
            return 'http://movie.douban.com/top250' + m.group()
l,t = getlists(url)
# 当存在下一页链接时，运行
while nexturl(url):
    url = nexturl(url)
    a,b = getlists(url)
    l,t = l+a,t+b
# 最终链接保存在数组l，标题保存在数组t

# 按照给定格式打印出来
for i in range(0,len(l)):
    print = '%s. [%s](%s)' % (str(i+1),t[i].decode('utf-8').encode('gbk'),l[i])