`<blockquote>`
#coding=utf-8

import urllib
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'href="(.+?.jpg)" da'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

html = getHtml("URL").decode('utf-8') 

i = 1
for n in getImg(html):
    urllib.request.urlretrieve(n,"ADDRESS/%s.jpg" %i) #ADDRESS which is the picture saved in
    print('%s/%s' %(i,len(getImg(html))))
    i += 1
print ('finish!')#ending mark
