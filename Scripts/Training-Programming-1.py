# -*- coding: UTF-8 -*-
from selenium import webdriver
import sys
import importlib
import urllib.parse
importlib.reload(sys)
# 1.用于将cookie字符串转换为对象，因为后面add_cookie需要传字典进去
def ParseCookiestr(cookie_str):
    cookielist = []
    for item in cookie_str.split(';'):
        cookie={}
        itemname=item.split('=')[0]
        iremvalue=item.split('=')[1]
        cookie['name']=itemname
        cookie['value']=urllib.parse.unquote(iremvalue)
        cookielist.append(cookie)
    return cookielist

if __name__ == '__main__':
    url='http://www.wechall.net/challenge/training/programming1/index.php?action=request'
    # 参数为文本形式的cookie,如：WC=yourwccookie
    cookie_str=sys.argv[1]
    cookielist=ParseCookiestr(cookie_str)
    driver = webdriver.Chrome()       # 打开 Chrome 浏览器
    driver.set_page_load_timeout(5000)    # 防止页面加载个没完
    # 2.需要先获取一下url，不然使用add_cookie会报错，这里有点奇怪
    driver.get(url)

    for i in cookielist:
        cookie = {}
        # 3.对于使用add_cookie来说，参考其函数源码注释，需要有name,value字段来表示一条cookie，有点生硬
        cookie['name'] = i['name']
        cookie['value']=i['value']
        # 4.这里需要先删掉之前那次访问时的同名cookie，不然自己设置的cookie会失效
        driver.delete_cookie(i['name'])
        # 添加自己的cookie
        driver.add_cookie(cookie)

    try:
        driver.get(url)  # 再次打开爬取页面
        print(driver.get_cookies()) # 打印设置成功的cookie
        tag=driver.find_element_by_xpath('/html/body')
        content=tag.text
        backurl='http://www.wechall.net/challenge/training/programming1/index.php?answer='+content
        driver.get(backurl)
        print('Sucess!')
    except:
        print("ERROR")