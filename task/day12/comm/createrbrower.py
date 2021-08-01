#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: createrbrower.py
@time: 2021/5/24 09:14
'''
import unittest
from selenium import webdriver
class Creater(unittest.TestCase):
    def setUp(self):
        # 测试执行之前执行
        print("正在启动浏览器...")
        self.driver = webdriver.Chrome()
        self.driver.get("http://shop.aircheng.com/site/index")
    def tearDown(self):
        # 测试执行之后执行
        self.driver.quit()