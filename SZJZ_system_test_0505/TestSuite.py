#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
from SZJZ_system_test_0505.TestCaseLogin import TestCaseLogin

report_dir = "./reports"
date = time.strftime('%Y%m%d', time.localtime())
# 文件
report_file = report_dir + f'/test_case_{date}_reports.html'
# 创建目录
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

with open(report_file, 'wb') as f:
    loader = unittest.TestLoader()
    suite = loader.discover('./', pattern='TestCase*.py')
    runner = HTMLTestRunner(title="神州信息系统_登录测试", description='测试人:卞福昊', stream=f)
    runner.run(suite)