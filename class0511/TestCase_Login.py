#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import requests
from ddt import ddt, file_data


@ddt
class Test_requests(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    @file_data("user.json")
    def test_login(self, username, password):
        params_login = {
            "username": username,
            "password": password
        }
        response = self.session.post("http://192.168.31.162:8888/doLogin", params=params_login)
        status_json = response.json()
        msg = status_json["msg"]
        self.assertEqual(msg, "登录成功")
        print(f"-----用户:{username},登录测试通过!-----")


if __name__ == '__main__':
    unittest.main()
