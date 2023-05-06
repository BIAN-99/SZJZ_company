#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    用于封装公共方法
"""
from telnetlib import EC

from selenium import webdriver
import time


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

    # 打开被测项目地址
    def open_url(self, url):
        self.driver.get(url)
        time.sleep(2)

    # 定位元素
    def find_element(self, locator):
        """
        定位单个元素,如果定位成功返回元素本身,如果失败,返回False
        :param locator: 定位器,例如("id","id属性值")
        :return: 元素本身
        """
        try:
            element = self.driver.find_element(locator[0], locator[1])
            return element
        except:
            print(f"{locator}元素没找到")
            return None

    # 点击操作
    def click(self, locator):
        """
            点击元素
            :return:
        """
        element = self.find_element(locator)
        element.click()

    # 输入操作
    def send_keys(self, locator, text):
        """
        元素输入
        :param locator: 定位器
        :param text: 输入内容
        :return:
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def close(self):
        time.sleep(2)
        self.driver.quit()
