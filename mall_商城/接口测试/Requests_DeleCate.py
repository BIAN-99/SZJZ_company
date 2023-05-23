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

    @file_data("data/delCateID.json")
    def test_add(self, id):

        headers = {
            'Authorization': 'Bearer' + ' ' + self.token
        }
        response = requests.post("http://192.168.31.162:8080/productCategory/delete/"+id, headers=headers)
        self.assertEqual(response.json()['code'], 200)
        print(f"-----{id}类删除测试成功!-----")


if __name__ == '__main__':
    unittest.main()