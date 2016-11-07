import urllib2
import os
def download(url,filename):
    try:
        conn = urllib2.urlopen(url,timeout=5)
        f = open(filename,'wb')
        f.write(conn.read())
        f.close()
        return True
    except urlli2.URLError:
        print ('load',url,'error')
        return False
    except Exception:
        print("unkown exception in conn.read()")
        return ''
pic_url = 'http://static.123rf.com.cn/public/images/corp/photo/20160310/corp-main-image.jpg'
file_path = 'D://abc'
download(pic_url,file_path)
print('over')