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

    @file_data("addinfo.json")
    def test_addinfo(self, name, age, degree, employeeGWId, major, originId, school, sex, telephone):
        params_login = {
            "age": age,
            "degree": degree,
            "employeeGWId": employeeGWId,
            "major": major,
            "name": name,
            "originId": originId,
            "school": school,
            "sex": sex,
            "telephone": telephone
        }
        # 如果请求头中content-type为application/x-www-form-urlencoded，为表单形式，post请求时使用使用data参数。
        # 如果请求头中content-type为application/json,  为json形式，post请求使用json参数。
        response = self.session.post("http://192.168.31.162:8888/cus/advanced/addCustomer", json=params_login)
        status_json = response.json()
        msg = status_json["msg"]
        self.assertEqual(msg, "添加成功")
        print(f"-----添加学员{name}信息,测试通过!-----")


if __name__ == '__main__':
    unittest.main()