# 开发人员 ：王阳
# 开发时间 ：2021/12/17 11:37
import urllib.request
import re
import os
import urllib   

import requests
from bs4 import BeautifulSoup

def get_html(url):
    page = urllib.request.urlopen(url)
    html_a = page.read()
    return html_a.decode('utf-8')

def makedir(fpath):
    if os.path.isdir(fpath) == False:
        os.makedirs(fpath)

def getImage(html,i):
    reg = r'https://[^\s]*\.jpg'#正则匹配串
    image = re.compile(reg)  # 转换成一个正则对象
    data = image.findall(html) # 表示在整个网页过滤出所有图片的地址，放在data中
    #print(data)
    fpath = 'E:/tiebaimage/page_'+str(i+1)
    makedir(fpath)#创建文件夹
    num = 0
    for url in data:
        r = requests.get(url)
        num +=1
        if num > 1 and data[num-1] == data[num-2]:
            continue
        with open(fpath+'/'+str(num) + "_image.png", 'wb') as fp:
            fp.write(r.content)

def main(kw = '',page = 1):

    if kw != '':
        url = "https://tieba.baidu.com/f?kw="+kw+'&ie=utf-8'
        for i in range(page):
            html = get_html(url+'&pn='+str(i*50))
            getImage(html,i)

main()
