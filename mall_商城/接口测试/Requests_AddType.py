#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import requests
from ddt import ddt, file_data


@ddt
class Test001(unittest.TestCase):

    def setUp(self) -> None:
        self.session = requests.session()
        params_login = {
            "username": "fuhao",
            "password": "123"
        }
        r = self.session.post("http://192.168.31.162:8080/admin/login", json=params_login)
        message = r.json()
        self.token = message['data']['token']

    def tearDown(self) -> None:
        self.session.close()

    @file_data("data/addType.json")
    def test001(self, name):
        headers = {
            'Authorization': 'Bearer'+' '+self.token
        }
        params_login = {
            "name": name
        }
        print(params_login)
        response = self.session.post("http://192.168.31.162:8080/productAttribute/category/create", params=params_login, headers=headers)
        self.assertEqual(response.status_code, 200)
        print(f"-----{name}类型添加测试成功!-----")


if __name__ == '__main__':
    unittest.main()
