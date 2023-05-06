#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from time import sleep

from ddt import ddt, file_data

from SZJZ_system_test_0505.SearchPage import SearchPage


@ddt
class TestCaseFind(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = SearchPage()
        self.driver.open_url(SearchPage.url)
        self.driver.login("fuhao", "123")
        sleep(2)
        self.driver.click_menu()
        sleep(2)
        self.driver.click_cust()
        sleep(1)

    @file_data("search_name_info.yaml")
    def test_find(self, username):
        self.driver.search_input(username)
        self.driver.click_search()
        self.assertIsNotNone(self.driver.searchinfo())
