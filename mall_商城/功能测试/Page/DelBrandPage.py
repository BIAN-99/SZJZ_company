#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from mall_0518.功能测试.BasePage import Base


class DelBrandPage(Base):
    username_input_locator = (By.NAME, "username")
    password_input_locator = (By.NAME, "password")
    login_button_locator = (By.CSS_SELECTOR, ".el-form-item__content>.el-button--primary")
    product_locator = (By.CSS_SELECTOR, ".el-submenu>.el-submenu__title")
    productBrand_locator = (By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/div/li[1]/ul/a[5]/li/span')
    search_brand_locator = (By.CSS_SELECTOR, '[placeholder="品牌名称/关键字"]')
    search_btn_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/button')
    del_btn_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/table/tbody/tr[1]/td[9]/div/button[2]/span')
    confirm_btn_locator = (By.CSS_SELECTOR, ".el-message-box__btns>.el-button--primary")
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

    # 封装点击到品牌管理界面操作
    def tobrand(self):
        self.get_element(self.product_locator).click()
        self.get_element(self.productBrand_locator).click()

    # 封装添加操作
    def delbrand(self, brand):
        self.get_element(self.search_brand_locator).send_keys(brand)
        self.get_element(self.search_btn_locator).click()
        self.get_element(self.del_btn_locator).click()
        self.get_element(self.confirm_btn_locator).click()

    def getMessage(self):
        message = self.get_element(self.message_locator)
        return message.get_property("innerText")
