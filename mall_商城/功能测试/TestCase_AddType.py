#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest

from ddt import ddt, file_data

from mall_商城.功能测试.Page.AddType import AddTypePage


@ddt
class TestAdd(unittest.TestCase):
    def setUp(self) -> None:
        """
              前置函数
              用于打开浏览器，连接数据库，初始化数据等操作
          """
        # 2. 打开谷歌浏览器（获取浏览器操作对象,并登录）
        self.driver = AddTypePage()
        self.driver.open_url(AddTypePage.url)
        self.driver.login()

    def tearDown(self) -> None:
        self.driver.close()

    @file_data("data/Type.yaml")
    def test_001(self, Type):
        self.driver.toproductType()
        self.driver.addType(Type)
        print(f"-----成功添加类型{Type},测试成功!-----")