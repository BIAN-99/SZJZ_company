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

    @file_data("data/attriBatchDel.json")
    def test_add(self, ids):
        data = {
            "ids": ids
        }
        headers = {
            'Authorization': 'Bearer' + ' ' + self.token
        }
        response = requests.post("http://192.168.31.162:8080/productAttribute/delete", params=data,
                                 headers=headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        print(f"-----属性{ids}批量删除测试成功!-----")


if __name__ == '__main__':
    unittest.main()
