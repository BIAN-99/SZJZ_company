#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    管理登陆页面所有的元素，
    以及操作这些元素所用的方法。
"""
from selenium.webdriver.common.by import By

from SZJZ_system_test_0505.BasePage import Base


class LoginPage(Base):
    # 编写定位器及页面属性
    name_input_locator = (By.ID, "username")
    passwd_input_locator = (By.ID, "password")
    submit_button_locator = (By.CLASS_NAME, "loginButton")
    url = 'http://192.168.31.162:8889'

    # """封装元素操作"""
    # 输入用户名
    def name_input(self, username):
        self.click(self.name_input_locator)
        self.send_keys(self.name_input_locator, username)

    # 输入密码
    def passwd_input(self, password):
        self.send_keys(self.passwd_input_locator, password)

    # 点击登陆
    def click_submit(self):
        self.click(self.submit_button_locator)

    # 获取提示信息框
    def findHomeWelcome(self):
        return self.find_element((By.CLASS_NAME, 'homeWelcome'))



