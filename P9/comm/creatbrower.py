#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: creatbrower.py
@time: 2021/5/23 15:15
'''

import unittest
from selenium import webdriver

class CreaterBrowser(unittest.TestCase):
    # 初始化
    def setUp(self):  # 定义一次 自动调用，每一次执行测试用例之前都会调用setUp()
        print("操作之前")
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    # 执行测试后的清除工作
    def tearDown(self):  # 定义一次 自动调用，每一次执行测试用例之后都会调用tearDown()
        print("操作之后")
        self.driver.quit()