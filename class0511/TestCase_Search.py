#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import requests
from ddt import ddt, file_data


@ddt
class Test_requests(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.params_login = {
            "username": "fuhao",
            "password": "123"
        }
        self.session.post("http://192.168.31.162:8888/doLogin", params=self.params_login)

    def tearDown(self) -> None:
        self.session.close()

    @file_data("searchinfo.json")
    def test_addinfo(self, size, page):
        params_login = {
            "size": size,
            "page": page
        }
        response = self.session.get("http://192.168.31.162:8888/cus/advanced/getAllCustomer", params=params_login)
        status_json = response.json()
        total = status_json["total"]
        self.assertIsNotNone(total)
        print(f"-----搜索信息,测试通过!-----")


if __name__ == '__main__':
    unittest.main()