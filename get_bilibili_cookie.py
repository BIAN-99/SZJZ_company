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

# 浏览器界面最大化
driver.maximize_window()
sleep(20)
# 首先清除由于浏览器打开已有的cookies
driver.delete_all_cookies()
with open('cookies.txt', 'w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.close()
