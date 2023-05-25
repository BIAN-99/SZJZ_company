#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from mall_0518.功能测试.BasePage import Base


class AddBrandPage(Base):
    username_input_locator = (By.NAME, "username")
    password_input_locator = (By.NAME, "password")
    login_button_locator = (By.CSS_SELECTOR, ".el-form-item__content>.el-button--primary")
    product_locator = (By.CSS_SELECTOR, ".el-submenu>.el-submenu__title")
    productBrand_locator = (By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/div/li[1]/ul/a[5]/li/span')
    add_btn_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div/button/span')
    brand_name_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/form/div[1]/div/div[1]/input')
    brand_first_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/form/div[2]/div/div/input')
    brand_uplogo_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/form/div[3]/div/div/div[1]/div[1]/input')
    brand_submmit_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/form/div[9]/div/button[1]/span')
    confirm_locator = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')
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
    def addbrand(self, name, first, logo):
        self.get_element(self.add_btn_locator).click()
        self.get_element(self.brand_name_locator).click()
        self.get_element(self.brand_name_locator).send_keys(name)
        self.get_element(self.brand_first_locator).click()
        self.get_element(self.brand_first_locator).send_keys(first)
        self.get_element(self.brand_uplogo_locator).send_keys(logo)
        self.get_element(self.brand_submmit_locator).click()
        self.get_element(self.confirm_locator).click()

    # # 获取提示信息
    # def getInfo(self):
    #     message = self.get_element(self.success_locaotor).get_property("innerText")
    #     return message
