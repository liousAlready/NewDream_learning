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
from P9.comm import creatbrower


class TestLink(creatbrower.CreaterBrowser):
    '''百度搜索测试用例'''

    # # 初始化
    # def setUp(self):  # 定义一次 自动调用，每一次执行测试用例之前都会调用setUp()
    #     print("操作之前")
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://www.baidu.com")
    #     self.handle = self.driver.current_window_handle
    #
    # # 执行测试后的清除工作
    # def tearDown(self):  # 定义一次 自动调用，每一次执行测试用例之后都会调用tearDown()
    #     print("操作之后")
    #     self.driver.quit()

    def swithwindows(self, linktest):
        self.handle = self.driver.current_window_handle
        self.driver.find_element_by_link_text(linktest).click()
        self.handles = self.driver.window_handles
        for h in self.handles:
            if h != self.handle:
                self.driver.switch_to.window(h)

    def test_news(self):
        '''测试点击新闻'''
        self.swithwindows("新闻")
        time.sleep(2)
        self.assertIn('news', self.driver.current_url)

    def test_hao123(self):
        '''测试点击hao123'''
        self.swithwindows("hao123")
        time.sleep(2)
        self.assertIn('hao', self.driver.current_url)

    def test_map(self):
        '''测试点击map'''
        self.swithwindows("地图")

        time.sleep(2)
        self.assertIn('map', self.driver.current_url)
