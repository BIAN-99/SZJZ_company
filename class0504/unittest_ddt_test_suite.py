#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from class0504 import MyTestCase_0504_002
from class0504.MyTestCase_0504_001 import TestCase001
from class0504.MyTestCase_0504_002 import TestCase002, TestCase003

# 第一种方法,一次添加一个测试方法
# 创建测试套件
suite1 = unittest.TestSuite()

# suite1.addTest(类名("方法名"))
suite1.addTest(TestCase001("test_001"))
suite1.addTest(TestCase001("test_002"))
suite1.addTest(TestCase002("test_003"))
suite1.addTest(TestCase002("test_004"))

# 实例化执行器
runner1 = unittest.TextTestRunner()

# 执行测试套件
runner1.run(suite1)
print("------------------------------------")

# 第二种方法,一次添加多个方法
# 创建测试套件
suite2 = unittest.TestSuite()
cases = [
    TestCase001('test_001'),
    TestCase001('test_002'),
    TestCase002('test_003'),
    TestCase002('test_004')
]
suite2.addTests(cases)
# 实例化执行器
runner2 = unittest.TextTestRunner()

# 执行测试套件
runner2.run(suite2)

print("------------------------------------")
# 第三种方法TestLoader
# 载入测试用例中所有的测试方法(装载器) - TestLoader
# loader = unittest.TestLoader()
# FromTestCase 通过类名
suite3 = unittest.defaultTestLoader.loadTestsFromTestCase(TestCase001)
runner3 = unittest.TextTestRunner()
runner3.run(suite3)
print("------------------------------------")
# FromName 通过模块名+类名,单个
suite4 = unittest.defaultTestLoader.loadTestsFromName('TestCase002', MyTestCase_0504_002)
runner4 = unittest.TextTestRunner()
runner4.run(suite4)
print("------------------------------------")
# FromNames 通过模块名+类名,多个
# suite5 = unittest.defaultTestLoader.loadTestsFromName(['TestCase002', 'TestCase003'], MyTestCase_0504_002)
# runner5 = unittest.TextTestRunner()
# runner5.run(suite5)
print("------------------------------------")
suite6 = unittest.defaultTestLoader.loadTestsFromModule(TestCase003())
runner6 = unittest.TextTestRunner()
runner6.run(suite6)
print("------------------------------------")
# 载入多个模块
# FromModule 通过加载器加载整个模块
suite7 = unittest.defaultTestLoader.discover('./', pattern='MyTestCase*')
runner7 = unittest.TextTestRunner()
runner7.run(suite7)


