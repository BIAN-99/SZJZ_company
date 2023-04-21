from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import json

# 获取浏览器设置对象
option = webdriver.EdgeOptions()

# 设置浏览器不自动退出
option.add_experimental_option('detach', True)

# 获取浏览器,并把以上设置传入

driver = webdriver.Edge(options=option)

# 获取浏览地址并打开
url = 'https://www.bilibili.com'
driver.get(url)
sleep(1)

# 首先清除由于浏览器打开已有的cookies
driver.delete_all_cookies()

with open('cookies.txt', 'r') as f:
    # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookies_list = json.load(f)
    for cookie in cookies_list:
        driver.add_cookie(cookie)
# 刷新浏览器界面,刷新后即显示登录后的界面
driver.refresh()