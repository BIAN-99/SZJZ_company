#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from mall_0518.功能测试.BasePage import Base


class AddTypePage(Base):
    username_input_locator = (By.NAME, "username")
    password_input_locator = (By.NAME, "password")
    login_button_locator = (By.CSS_SELECTOR, ".el-form-item__content>.el-button--primary")
    commodity_locator = (By.CSS_SELECTOR, ".el-submenu>.el-submenu__title")
    commodity_Type_locator = (By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/div/li[1]/ul/a[4]/li/span')
    add_type_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/button/span')
    name_input = (By.CSS_SELECTOR, '.el-input__inner')
    confirm_locator = (By.CSS_SELECTOR, '.dialog-footer>.el-button--primary')
    message_locator = (By.CSS_SELECTOR, '.el-message__content')
    url = "http://192.168.31.162:8090"

    # 封装登录操作
    def login(self):
        i = 0
        self.get_element(self.username_input_locator).click()
        while i < 5:
            self.send_keys(self.username_input_locator, Keys.BACKSPACE)
            i += 1
        self.get_element(self.username_input_locator).send_keys("fuhao")
        self.get_element(self.password_input_locator).send_keys("123")
        self.get_element(self.login_button_locator).click()

    # 封装点击到商品类型界面操作
    def toproductType(self):
        self.get_element(self.commodity_locator).click()
        self.get_element(self.commodity_Type_locator).click()

    # 封装添加操作
    def addType(self, Type):
        self.get_element(self.add_type_locator).click()
        self.get_element(self.name_input).send_keys(Type)
        self.get_element(self.confirm_locator).click()

    # 获取提示信息
    def getInfo(self):
        message = self.get_element(self.message_locator).get_property("innerText")
        return message
