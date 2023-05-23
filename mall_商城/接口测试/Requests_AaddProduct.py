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
    def test_add(self, brandId, brandName, description, giftGrowth, giftPoint, keywords, lowStock,
                 name, newStatus, note, originalPrice, price, productCategoryId, productCategoryName, productSn):
        headers = {
            'Authorization': 'Bearer' + ' ' + self.token,
            'Accept-Ranges': 'bytes',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        json_data = {
            "brandId": brandId,
            "brandName": brandName,
            "description": description,
            "giftGrowth": giftGrowth,
            "giftPoint": giftPoint,
            "keywords": keywords,
            "lowStock": lowStock,
            "name": name,
            "newStatus": newStatus,
            "note": note,
            "originalPrice": originalPrice,
            "price": price,
            "productCategoryId": productCategoryId,
            "productCategoryName": productCategoryName,
            "productSn": productSn
        }

        response = requests.post("http://192.168.31.162:8080/product/create", json=json_data,
                                 headers=headers)
        self.assertEqual(response.status_code, 200)
        # print(f"-----商品{name}添加测试成功!-----")
        print(response.status_code)
        print(response.json())


if __name__ == '__main__':
    unittest.main()
