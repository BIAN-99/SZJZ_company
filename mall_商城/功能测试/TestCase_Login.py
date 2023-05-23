#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest

from ddt import ddt, file_data

from mall_商城.功能测试.Page.LoginPage import LoginPage


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        """
              前置函数
              用于打开浏览器，连接数据库，初始化数据等操作
          """
        # 2. 打开谷歌浏览器（获取浏览器操作对象）
        self.driver = LoginPage()
        self.driver.open_url(LoginPage.url)

        # LoginPage.open_url(LoginPage.url)

    def tearDown(self) -> None:
        self.driver.close()

    @file_data("data/login_info.yaml")
    def test_login(self, username, password):
        self.driver.input_username(username)
        self.driver.input_password(password)
        self.driver.login()
        self.assertIsNotNone(self.driver.findLoginINfo())
        print(f"-----用户{username}登录测试成功-----")
