# coding=utf-8
'''
@File : createbrowser.py
@Time : 2021/5/23 15:15
@Author: luoman
'''
# import lib
import unittest

from selenium import webdriver

from P9.day_13_integration.iwebshop_selenium.comm.browseroperator import BrowswerOperator
from P9.day_13_integration.iwebshop_selenium.comm.config import Config
from P9.day_13_integration.iwebshop_selenium.comm.logs import Logging

log = Logging().getloger()
conf = Config()


class CreateBrowser(unittest.TestCase):
    # 初始化
    conf = Config()

    def getdriver(self, drivername):
        if drivername == 'chrome':
            self.driver = webdriver.Chrome()
            log.info("使用chrome浏览器")
        elif drivername == 'firfox':
            self.driver = webdriver.Firefox()
            log.info("使用火狐浏览器")

        elif drivername == 'edge':
            self.driver = webdriver.Edge()
            log.info("使用edge")

        else:
            self.driver = None
            log.error("创建浏览器失败")
            return self.driver

    def setUp(self):  # 调用是自动调用，每一次执行测试用例之前都会调用setUp()
        self.getdriver(conf.browsername)
        self.bo = BrowswerOperator(self.driver)
        self.bo.get_url(conf.url)

    # 执行测试后的清除工作
    def tearDown(self):  # 调用是自动调用，每一次执行测试用例之后都会调用setUp()
        self.driver.quit()
