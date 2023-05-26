#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner

report_dir = "./reports"
date = time.strftime('%Y%m%d', time.localtime())
# 文件
report_file = report_dir + f'/Unittest_{date}_reports.html'
# 创建目录
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

with open(report_file, 'wb') as f:
    loader = unittest.TestLoader()
    suite = loader.discover('./', pattern='TestCase*.py')
    runner = HTMLTestRunner(title="mall商城系统功能测试", description='测试人:卞福昊', stream=f)
    runner.run(suite)