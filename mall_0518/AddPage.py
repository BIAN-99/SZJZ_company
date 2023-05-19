#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from mall_0518.BasePage import Base


class AddPage(Base):
    username_input_locator = (By.NAME, "username")
    password_input_locator = (By.NAME, "password")
    login_button_locator = (By.CSS_SELECTOR, ".el-form-item__content>.el-button--primary")
    commodity_locator = (By.CSS_SELECTOR, ".el-submenu>.el-submenu__title")
    fenlei_locator = (By.XPATH, "//*[@id='app']/div/div[1]/div/ul/div/li[1]/ul/a[3]/li")
    addbtn_locator = (By.CSS_SELECTOR, ".btn-add")
    name_input_locator = (By.CSS_SELECTOR, ".el-form-item__content>.el-input>.el-input__inner")
    submit_btn_locator = (By.XPATH, "//*[@id='app']/div/div[2]/section/div/div/form/div[12]/div/button[1]")
    confirm_btn_locator = (By.CSS_SELECTOR, ".el-message-box__btns>.el-button--primary")
    success_locaotor = (By.CSS_SELECTOR, ".el-message--success")
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
    # 封装点击到商品分类界面操作
    def toproductCate(self):
        self.get_element(self.commodity_locator).click()
        self.get_element(self.fenlei_locator).click()

    # 封装添加操作
    def addproduct(self, name):
        self.get_element(self.addbtn_locator).click()
        self.get_element(self.name_input_locator).click()
        self.get_element(self.name_input_locator).send_keys(name)
        self.get_element(self.submit_btn_locator).click()
        self.get_element(self.confirm_btn_locator).click()

    # 获取提示信息
    def getInfo(self):
        message = self.get_element(self.success_locaotor).get_property("innerText")
        return message

