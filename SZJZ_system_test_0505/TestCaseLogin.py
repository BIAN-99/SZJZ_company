#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest

from ddt import ddt, file_data

from SZJZ_system_test_0505.LoginPage import LoginPage


@ddt
class TestCaseLogin(unittest.TestCase):
    def setUp(self) -> None:
        """
              前置函数
              用于打开浏览器，连接数据库，初始化数据等操作
          """
        # 2. 打开谷歌浏览器（获取浏览器操作对象）
        self.driver = LoginPage()
        self.driver.open_url(LoginPage.url)

    def tearDown(self) -> None:
        # 5. 关闭浏览器
        self.driver.close()

    @file_data("login_info.yaml")
    def test_Login(self, username, password):
        """登陆测试用例"""
        self.driver.name_input(username)
        self.driver.passwd_input(password)
        self.driver.click_submit()
        self.assertIsNotNone(self.driver.findHomeWelcome())

