#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest


class TestCase001(unittest.TestCase):
    def test_001(self):
        self.assertEqual(1, 2)
        print("测试001")

    def test_002(self):
        print(测试002)
