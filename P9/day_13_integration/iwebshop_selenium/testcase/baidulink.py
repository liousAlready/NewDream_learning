#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: baidulink.py
@time: 2021/5/23 11:26
'''
# 1.引入unittest
import unittest
from selenium import webdriver
import time
import P9.day_13_integration.iwebshop_selenium.comm
from selenium.webdriver.common.by import By


class TestLink(P9.day_13_integration.iwebshop_selenium.comm.createbrowser.CreateBrowser):
    '''百度搜索测试用例'''

    def test_news(self):
        '''测试点击新闻'''
        self.bo.swithwindows(By.LINK_TEXT, "新闻")
        time.sleep(2)
        self.assertIn('news', self.driver.current_url)

    def test_hao123(self):
        '''测试点击hao123'''
        self.bo.swithwindows(By.LINK_TEXT, "hao123")
        time.sleep(2)
        self.assertIn('hao', self.driver.current_url)

    def test_map(self):
        '''测试点击map'''
        self.bo.swithwindows(By.LINK_TEXT, "地图")

        time.sleep(2)
        self.assertIn('map', self.driver.current_url)


if __name__ == '__main__':
    def createsuite():
        # 定义一个测试套件对象
        suite = unittest.TestSuite()
        # 把用例装载到套件中
        suite.addTest(TestLink('test_map'))

        return suite


    unittest.main(defaultTest='createsuite')
