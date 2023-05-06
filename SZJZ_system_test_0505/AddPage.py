#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    管理添加页面所有的元素，
    以及操作这些元素所用的方法。
"""
from selenium.webdriver.common.by import By

from SZJZ_system_test_0505.BasePage import Base


class AddPage(Base):
    cust_button_locator = (By.XPATH, "/html/body/div/section/section/aside/div/div[1]/div/ul/li[1]/ul/li")
    name_input_locator = (By.ID, "username")
    passwd_input_locator = (By.ID, "password")
    submit_button_locator = (By.CLASS_NAME, "loginButton")
    search_input_locator = (By.CLASS_NAME, "el-input__inner")
    search_button_locator = (By.CLASS_NAME, "el-icon-search")
    menu_button_locator = (By.CSS_SELECTOR, ".fa-money")
    add_button_locator = (By.CLASS_NAME, "el-icon-plus")
    uname_input_locator = (By.ID, 'name')
    sex_input_locator = (By.CSS_SELECTOR, " .el-radio__input>.el-radio__inner")
    phone_input_locator = (By.ID, "phone")
    info_select_locator = (By.ID, "origin")
    zhilian_locator =(By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[4]/span[text()='智联投递']")
    degree_selector_locator = (By.ID, "degree")
    benke_locator = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[1]/span[text()='本科']")
    age_input_locator = (By.ID, "age")
    school_input_locator = (By.ID, "school")
    major_input_locator = (By.ID, "major")
    guwen_select_locator = (By.ID, "employeeGW")
    juan_locator = (By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[1]/span[text()='娟娟']")
    confirm_locator = (By.CSS_SELECTOR, '.dialog-footer>button.el-button.el-button--primary')
    url = 'http://192.168.31.162:8889'
    # """封装元素操作"""
    # 输入要添加的用户信息

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

    # 点击添加按钮
    def click_add(self):
        self.click(self.add_button_locator)

    # 输入姓名
    def uname_input(self, uname):
        self.send_keys(self.uname_input_locator, uname)

    # 选择性别
    def sex_input(self):
        self.click(self.sex_input_locator)

    # 输入手机号
    def phoneNum_input(self, phone):
        self.send_keys(self.phone_input_locator, phone)

    # 选择信息来源
    def info_select(self):
        self.click(self.info_select_locator)
        self.click(self.zhilian_locator)

    # 选择学历
    def degree_select(self):
        self.click(self.degree_selector_locator)
        self.click(self.benke_locator)

    # 输入年龄
    def age_input(self, age):
        self.send_keys(self.age_input_locator, age)

    # 输入学校
    def school_input(self, school):
        self.send_keys(self.school_input_locator, school)

    # 输入专业
    def major_input(self, major):
        self.send_keys(self.major_input_locator, major)

    # 选择顾问
    def guwen_select(self):
        self.click(self.guwen_select_locator)
        self.click(self.juan_locator)

    # 确定
    def confirm(self):
        self.click(self.confirm_locator)

    # 获取提示信息
    def addinfo(self):
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-message>.el-message__content')
        return message.get_property('innerText')

    # 刷新
    def refresh(self):
        self.driver.refresh()
