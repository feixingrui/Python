#coding=utf-8

import urllib
import urllib.request
import re
import time

def timetime():
    return time.strftime("%y%m%d",time.localtime(time.time()))

def getCYBNews(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    reg = r'<a target="_blank" href="(.+/20%s/.+.html)" class="item-title">' %(timetime())
    #reg = r'<a target="_blank" href="(.+/20160417/.+.html)" class="item-title">'
    newsre = re.compile(reg)
    newslist = re.findall(newsre,html)
    i = 1
    news = ''
    for n in newslist:
        sub_page = urllib.request.urlopen(n)
        sub_html = sub_page.read().decode('utf-8')
        sub_reg = r'<h1 class="article-tit">(.{1,50})</h1>'
        sub_newsre = re.compile(sub_reg)
        sub_newslist = re.findall(sub_newsre,sub_html)
        if not len(sub_newslist):
            continue
        news += '%d.%s\n \n' %(i,sub_newslist[0])
        i += 1
        if i%5 == 1:
            news = news + '----------------------\n \n'
    news = u'早安！\n每天早晨拥抱你，真好～\n \n----------------------\n▼\n \n' + news
    return news

print('Today is: %s\n\n' %(timetime()))
content = getCYBNews('http://www.cyzone.cn/category/8/')
content = content + '来自创业邦'
print(content)


