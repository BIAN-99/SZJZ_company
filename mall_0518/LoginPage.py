#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from mall_0518.BasePage import Base


class LoginPage(Base):
    username_input_locator = (By.NAME, "username")
    password_input_locator = (By.NAME, "password")
    login_button_locator = (By.CSS_SELECTOR, ".el-form-item__content>.el-button--primary")
    url = "http://192.168.31.162:8090"

    # 封装输入用户名操作
    def input_username(self, username):
        i = 0
        self.get_element(self.username_input_locator).click()
        while i < 5:
            self.send_keys(self.username_input_locator, Keys.BACKSPACE)
            i += 1
        self.send_keys(self.username_input_locator, username)

    # 封装输入密码操作
    def input_password(self, password):
        self.send_keys(self.password_input_locator, password)

    # 登录操作
    def login(self):
        self.click(self.login_button_locator)

    # 获取提示信息框
    def findLoginINfo(self):
        return self.get_element((By.CLASS_NAME, 'menu-wrapper'))
