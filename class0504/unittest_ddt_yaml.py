#!/usr/bin/python
# -*- coding: UTF-8 -*-


import unittest
from ddt import ddt, unpack, data, file_data


@ddt
class TestPhone(unittest.TestCase):
    @file_data("phoneNum.yaml")
    def test_001_phone(self, phone):
        print("测试手机号 : ", phone)

    @file_data("userInfo.yaml")
    @unpack
    def test_002_info(self, id, name, age):
        print("测试id : ", id)
        print("测试姓名 : ", name)
        print("测试年龄 : ", age)


if __name__ == "__main__":
    unittest.main()
