#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import unittest
import requests
from ddt import ddt, file_data, unpack


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

    @file_data("data/change.json")
    def test_add(self, re_data):
        json_data = json.dumps(re_data)
        headers = {
            'Authorization': 'Bearer' + ' ' + self.token
        }
        response = requests.post("http://192.168.31.162:8080/product/update/37", json=json_data,
                                 headers=headers)
        print(response.status_code)
        print(response.json())
        # self.assertEqual(response.status_code, 200)
        # print(f"-----id为{id}的商品更新测试成功!-----")


if __name__ == '__main__':
    unittest.main()
