#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import requests
from ddt import ddt, file_data


@ddt
class Test001(unittest.TestCase):

    def setUp(self) -> None:
        params_login = {
            "username": "fuhao",
            "password": "123"
        }
        r = requests.post("http://192.168.31.162:8080/admin/login", json=params_login)
        message = r.json()
        self.token = message['data']['token']

    @file_data("data/addproduct.json")
    def test_add(self, data):
        headers = {
            'Authorization': 'Bearer' + ' ' + self.token,
        }
        print(data[0])
        response = requests.post("http://192.168.31.162:8080/product/create", json=data[0],
                                 headers=headers)
        self.assertEqual(response.status_code, 200)
        # print(f"-----商品{name}添加测试成功!-----")
        print(response.status_code)
        print(response.json())


if __name__ == '__main__':
    unittest.main()
