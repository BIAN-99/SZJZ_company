#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import os
from HTMLTestRunner_PY3 import HTMLTestRunner
# 目录
report_dir = "./reports"
# 在目录下创建文件
report_file = report_dir + '/html_reports.html'
# 若目录不存在,创建目录
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

with open(report_file, 'wb') as f:
    # 第三种方法TestLoader
    loader = unittest.TestLoader()
    # FromModule 通过加载器加载整个模块
    suite = loader.discover('./', pattern='MyTestCase*')
    # title放测试报告标题,description放测试报告的描述,stream放打开的文件,用于承载测试报告
    runner = HTMLTestRunner(title='5月4日模拟测试', description='此日学习使用了测试套件进行测试用例及测试方法的测试', stream=f)
    runner.run(suite)