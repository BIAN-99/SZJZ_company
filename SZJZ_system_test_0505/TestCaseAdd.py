#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from time import sleep

from ddt import ddt, file_data

from SZJZ_system_test_0505.AddPage import AddPage


@ddt
class TestCaseAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = AddPage()
        cls.driver.open_url(AddPage.url)
        cls.driver.login("fuhao", "123")
        sleep(2)
        cls.driver.click_menu()
        sleep(2)
        cls.driver.click_cust()
        sleep(1)

    def setUp(self) -> None:
        self.driver.refresh()
        self.driver.click_add()

    @file_data("add_info.yaml")
    def test_add(self, uname, phone, age, school, major):
        self.driver.uname_input(uname)
        self.driver.sex_input()
        self.driver.phoneNum_input(phone)
        self.driver.info_select()
        self.driver.degree_select()
        self.driver.age_input(age)
        self.driver.school_input(school)
        self.driver.major_input(major)
        self.driver.guwen_select()
        self.driver.confirm()
        self.assertEqual(self.driver.addinfo(), "添加成功")

