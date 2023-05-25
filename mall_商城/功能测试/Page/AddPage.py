#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from mall_0518.功能测试.BasePage import Base


class AddPage(Base):
    username_input_locator = (By.NAME, "username")
    password_input_locator = (By.NAME, "password")
    login_button_locator = (By.CSS_SELECTOR, ".el-form-item__content>.el-button--primary")
    product_locator = (By.CSS_SELECTOR, ".el-submenu>.el-submenu__title")
    product_add_locator = (By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/div/li[1]/ul/a[2]/li/span')
    product_cate_locator = (By.CSS_SELECTOR, ".el-cascader__label")
    product_cateitem1_locator = (By.CSS_SELECTOR, '.el-cascader-menu>.el-cascader-menu__item')
    product_cateitem2_locator = (By.XPATH, '/html/body/div[2]/ul[2]/li[2]')
    name_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[2]/div/div[1]/input')
    subtitle_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[2]/form/div[3]/div/div[1]/input')
    brand_locator = (By.CSS_SELECTOR, '.el-select__caret')
    brand_item = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[2]')
    next1_locator = (By.CSS_SELECTOR, '.el-button--primary')
    next2_locator = (By.XPATH, '/html/body/div[1]/div/div[2]/section/div/div/div[3]/form/div[17]/div/button[2]/span')
    upload_pic_locator = (By.CSS_SELECTOR, '.el-upload__input')
    next3_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[4]/form/div[6]/div/button[2]/span')
    submmit_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[5]/form/div[3]/div/button[2]/span')
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
    def toproductAdd(self):
        self.get_element(self.product_locator).click()
        self.get_element(self.product_add_locator).click()

    # 封装添加操作
    def addproduct(self, name, subTitle, pic):
        self.get_element(self.product_cate_locator).click()
        self.get_element(self.product_cateitem1_locator).click()
        self.get_element(self.product_cateitem2_locator).click()
        self.get_element(self.name_locator).send_keys(name)
        self.get_element(self.subtitle_locator).send_keys(subTitle)
        self.get_element(self.brand_locator).click()
        self.get_element(self.brand_item).click()
        self.get_element(self.next1_locator).click()
        self.get_element(self.next2_locator).click()
        self.get_element(self.upload_pic_locator).send_keys(pic)
        self.get_element(self.next3_locator).click()
        self.get_element(self.submmit_locator).click()
        self.get_element(self.confirm_btn_locator).click()

    # # 获取提示信息
    # def getInfo(self):
    #     message = self.get_element(self.success_locaotor).get_property("innerText")
    #     return message
