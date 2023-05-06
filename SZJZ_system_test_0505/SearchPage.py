#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    管理搜索页面所有的元素，
    以及操作这些元素所用的方法。
"""
from selenium.webdriver.common.by import By

from SZJZ_system_test_0505.BasePage import Base


class SearchPage(Base):
    name_input_locator = (By.ID, "username")
    passwd_input_locator = (By.ID, "password")
    submit_button_locator = (By.CLASS_NAME, "loginButton")
    search_input_locator = (By.CLASS_NAME, "el-input__inner")
    search_button_locator = (By.CLASS_NAME, "el-icon-search")
    menu_button_locator = (By.CSS_SELECTOR, ".fa-money")
    cust_button_locator = (By.XPATH, "/html/body/div/section/section/aside/div/div[1]/div/ul/li[1]/ul/li")
    url = 'http://192.168.31.162:8889'

    # """封装元素操作"""
    # 输入要搜索的用户姓名
    def search_input(self, username):
        self.send_keys(self.search_input_locator, username)

    # 登录
    def login(self, username, password):
        self.send_keys(self.name_input_locator, username)
        self.send_keys(self.passwd_input_locator, password)
        self.click(self.submit_button_locator)

    # 点击菜单
    def click_menu(self):
        self.click(self.menu_button_locator)

    # 点击客户资料
    def click_cust(self):
        self.click(self.cust_button_locator)

    # 点击搜索
    def click_search(self):
        self.click(self.search_button_locator)

    # 获取搜索后信息
    def searchinfo(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.el-pagination__total')

    # 隐式等待
    def wait(self, time):
        self.driver.implicitly_wait(time)
