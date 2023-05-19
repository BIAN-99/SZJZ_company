#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

from selenium import webdriver


class Base:
    # 初始化浏览器
    def __init__(self, browser="chrome", timeout=10):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        else:
            print("请输入正确的浏览器名称,例如:chrome,firefox,edge")

        # 隐式等待
        self.driver.implicitly_wait(timeout)

    # 打开目标地址
    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(1)

    # 定位元素
    def get_element(self, locator):
        try:
            element = self.driver.find_element(locator[0], locator[1])
            return element
        except:
            print(f"{locator}无法定位")
            return None

    # 点击操作
    def click(self, locator):
        element = self.get_element(locator)
        element.click()

    # 输入操作
    def send_keys(self, locator, text):
        element = self.get_element(locator)
        element.send_keys(text)

    # 关闭
    def close(self):
        self.driver.quit()

