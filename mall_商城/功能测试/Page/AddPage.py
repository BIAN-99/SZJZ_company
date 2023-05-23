#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from mall_商城.功能测试.Page.BasePage import Base


class AddPage(Base):
    username_input_locator = (By.NAME, "username")
    password_input_locator = (By.NAME, "password")
    login_button_locator = (By.CSS_SELECTOR, ".el-form-item__content>.el-button--primary")
    product_locator = (By.CSS_SELECTOR, ".el-submenu>.el-submenu__title")
    product_add_locator = (By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/div/li[1]/ul/a[2]/li/span')
    select_cate_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[1]/div/span/span')
    select_pre_item = (By.XPATH, '/html/body/div[2]/ul[1]/li[2]')
    select_item_locator = (By.XPATH, "/html/body/div[2]/ul[2]/li[2]")
    name_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[2]/div/div[1]/input')
    title_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[3]/div/div[1]/input')
    brand_locator = (By.CSS_SELECTOR, "[placeholder='请选择品牌']")
    brand_item_locator = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[4]/span')
    next1_btn_locator = (By.TAG_NAME, "button")
    next2_btn_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/form/div[17]/div/button[2]/span')
    next3_btn_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[4]/form/div[6]/div/button[2]/span')
    submit_btn_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[5]/form/div[3]/div/button[2]/span')
    confirm_locator = (By.CSS_SELECTOR, ".el-message-box__btns>.el-button--primary")
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

    # 封装点击到商品添加界面操作
    def toproductadd(self):
        self.get_element(self.product_locator).click()
        self.get_element(self.product_add_locator).click()

    # 封装添加操作
    def addproduct(self, name, subTitle):
        self.get_element(self.select_cate_locator).click()
        self.get_element(self.select_pre_item).click()
        self.get_element(self.select_item_locator).click()
        self.get_element(self.name_locator).send_keys(name)
        self.get_element(self.title_locator).send_keys(subTitle)
        self.get_element(self.brand_locator).click()
        self.get_element(self.brand_item_locator).click()
        self.get_element(self.next1_btn_locator).click()
        self.get_element(self.next2_btn_locator).click()
        self.get_element(self.next3_btn_locator).click()
        self.get_element(self.submit_btn_locator).click()
        self.get_element(self.confirm_locator).click()
    #
    # # 获取提示信息
    # def getInfo(self):
    #     message = self.get_element(self.success_locaotor).get_property("innerText")
    #     return message
    #
