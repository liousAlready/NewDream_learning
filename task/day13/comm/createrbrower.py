#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: createrbrower.py
@time: 2021/5/24 09:14
'''
import unittest
from selenium import webdriver
from task.day13.comm.browsereperator import Browsereperator
from task.day13.comm.config import Config
from task.day13.comm.logger import log

conf = Config()


class CreaterBrower(unittest.TestCase):

    def get_driver(self, drivername):
        conf = Config()
        '''获取浏览器的驱动'''
        if drivername == 'chrome':
            log.info("正在打开chrome...")
            self.driver = webdriver.Chrome()
        elif drivername == 'firfox':
            log.info("正在打开firfox...")
            self.driver = webdriver.Firefox()
        elif drivername == 'edge':
            log.info("正在打开edge...")
            self.driver = webdriver.Edge()
        else:
            log.error("输入的浏览器驱动错误，请重新检查！")
            self.driver = None
            return self.driver

    def setUp(self):
        # 测试执行之前执行
        log.info("正在启动浏览器...")
        self.get_driver(conf.browsername)
        self.bo = Browsereperator(self.driver)
        self.bo.get_url(conf.url)

    def tearDown(self):
        # 测试执行之后执行
        log.info("用例执行完毕，正在清除数据...")
        self.driver.quit()
