#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import requests
from ddt import ddt, file_data


@ddt
class Test001(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    @file_data("addproduct.json")
    def test001(self, id, product_id, product_sku_id,  member_id, quantity, price, product_name, product_sub_title):
        params_login = {
            "id": id,
            "product_id": product_id,
            "product_sku_id": product_sku_id,
            "member_id": member_id,
            "quantity": quantity,
            "price": price,
            "product_name": product_name,
            "product_sub_title": product_sub_title,
        }
        print(params_login)
        # response = self.session.get("http://192.168.31.162:8090/#/pms/addProduct", params=params_login)
        # print(response.status_code)



if __name__ == '__main__':
    unittest.main