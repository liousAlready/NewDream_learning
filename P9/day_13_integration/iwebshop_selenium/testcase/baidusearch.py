#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: baidusearch.py
@time: 2021/5/23 09:37
'''

# 1.引入unittest
import unittest
from selenium import webdriver
import time
import P9.day_13_integration.iwebshop_selenium.comm

version = '1.3'


class TestBaidu(P9.day_13_integration.iwebshop_selenium.comm.createbrowser.CreateBrowser):
    '''测试百度的测试用例'''

    # def __init__(self):
    #     self.kw = self.driver.find_element_by_id("kw")
    #     self.su = self.driver.find_element_by_id("su")

    def serch(self, keyword):
        self.driver.find_element_by_id("kw").send_keys(keyword)
        self.driver.find_element_by_id("su").click()

    # 写测试用例
    def test_serch1(self):
        '''测试正常功能的用例'''
        self.serch("python")
        time.sleep(2)
        self.assertIn('python', self.driver.title)

    @unittest.skip("该用例对应的功能已经被删除")
    def test_serch2(self):
        '''测试包含特殊字符的用例'''
        self.serch("python??")
        time.sleep(2)
        self.assertIn('python', self.driver.title)

    @unittest.expectedFailure
    def test_serch3(self):
        '''测试不输入内容的测试用例'''
        self.serch("python")
        time.sleep(2)
        self.assertIn('百度一下', self.driver.title)
