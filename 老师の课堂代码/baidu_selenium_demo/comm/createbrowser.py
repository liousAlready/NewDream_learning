'''
@File : createbrowser.py
@Time : 2021/5/23 15:15
@Author: luoman
'''
# import lib
import unittest
from selenium import webdriver
from 老师の课堂代码.baidu_selenium_demo.comm.browseroperator import BrowserOperator
from 老师の课堂代码.baidu_selenium_demo.comm.logger import log
from 老师の课堂代码.baidu_selenium_demo.comm.config import Config

conf = Config()
class CreateBrowser(unittest.TestCase):
    # 初始化
    # 第一次改进，对浏览器的类型进行选择
    conf = Config()
    def getdriver(self, drivename):
        if drivename == 'chrome':
            self.driver = webdriver.Chrome()
            log.info('创建谷歌浏览器')
        elif drivename == 'firefox':
            self.driver = webdriver.Firefox()
        elif drivename == 'edge':
            self.driver = webdriver.Edge()
        else:
            self.driver = None
            log.error('创建浏览器失败')
            return self.driver


    def setUp(self):  # 调用是自动调用，每一次执行测试用例之前都会调用setUp()
        self.getdriver(conf.browsername)
        self.bo = BrowserOperator(self.driver)
        self.bo.get_url(conf.url)


    # 执行测试后的清除工作
    def tearDown(self):  # 调用是自动调用，每一次执行测试用例之后都会调用setUp()
        self.driver.quit()