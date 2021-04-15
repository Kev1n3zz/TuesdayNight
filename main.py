# coding=utf-8
# demo source from url：https://blog.csdn.net/aaronjny/article/details/77945329
#
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.baidu.com')  # 请求百度首页
print(resp)  # 打印请求结果的状态码
print(resp.content)  # 打印请求到的网页源码

bsobj = BeautifulSoup(resp.content, 'lxml')  # 将网页源码构造成BeautifulSoup对象，方便操作
a_list = bsobj.find_all('a')  # 获取网页中的所有a标签对象
text = ''
for a in a_list:
    href = a.get('href')  # 获取a标签对象的href属性，就是这个对象指向的链接地址
    text += str(href) + '\n'  # 加入字符串后换行
with open('url.txt', 'w') as f:
    f.write(text)
