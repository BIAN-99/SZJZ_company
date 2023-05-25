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

    @file_data("data/change.json")
    def test_add(self, albumPics, id, brandId, brandName, description, giftGrowth, giftPoint, keywords,
                 lowStock, name, newStatus, note, originalPrice, price, productCategoryId, productCategoryName, productSn):
        data = {
            "albumPics": albumPics,
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
        headers = {
            'Authorization': 'Bearer' + ' ' + self.token
        }
        response = requests.post("http://192.168.31.162:8080/product/update/"+id, json=data,
                                 headers=headers)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        print(f"-----id为{id}的商品更新测试成功!-----")


if __name__ == '__main__':
    unittest.main()
