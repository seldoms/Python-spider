import urllib.request
import re
import os
import time

shuru=input("请输入:")
keyword=urllib.request.quote(shuru)
print(keyword)
file="E:\\meizhi-image\\"+str(shuru)
os.mkdir(file)
os.chdir(file)
list=[]
for url in range(0,1):
	list.append("http://www.soku.com/search_video_ajax/q_"+str(keyword)+"_orderby_1_limitdate_0?site=14&page="+str(url))

list1=[]
for eachlist in list: 
	url=urllib.request.urlopen(eachlist).read().decode("utf-8")
	neirong=re.findall("v-link\">(.*?)<i class=\"btn_play\">",url,re.S)
	for eachneirong in neirong:
		title=re.findall("a title=\"(.*?)\" target",eachneirong,re.S)
		logid=re.findall("log_vid=\"(.*?)\"",eachneirong,re.S)
		title1="".join(title)
#		print(title1)
		logid1="".join(logid)
		videourl="http://v.youku.com/v_show/id_"+str(logid1)+".html"
		videojs="<p><iframe width=\"845px\" height=\"600px\" src=\"http://v.youku.com/v_show/id_"+str(logid1)+"/v.swf\" frameborder=\"0\" border=\"0\""
		print(title1+" "+logid1+" "+videourl+" "+videojs)
		f=open("123.txt","a+")
		try:
			f.write(title1+"%"+logid1+"%"+videourl+"%"+videojs+"\n")
		except UnicodeEncodeError:
			continue
		f.close()
	img=re.findall("src=\"(.*?)\"",url,re.S)
	for eachimg in img:
		list1.append(eachimg+".jpg")

for eachlist1 in list1:
	print(eachlist1)
	imgname=re.findall("com\/(.*?).jpg",eachlist1,re.S)
	print(imgname)
	path="".join(imgname)
	print(path)
	path1=(path+".jpg")
	time.sleep(1)
	image = urllib.request.urlopen(eachlist1)
	image1 = image.read()
	f = open(path1, 'wb')1
	f.write(image1)
	f.close()