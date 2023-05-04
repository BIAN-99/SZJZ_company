#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


class TestCase002(unittest.TestCase):
    def test_003(self):
        print("测试003")

    def test_004(self):
        print("测试004")


class TestCase003(unittest.TestCase):
    def test_005(self):
        print("测试005")

    def test_006(self):
        a = 1
        self.assertIsNone(a)
        print("测试006")
