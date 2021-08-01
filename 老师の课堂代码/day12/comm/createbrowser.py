'''
@File : createbrowser.py
@Time : 2021/5/23 15:15
@Author: luoman
'''
# import lib
import unittest
from selenium import webdriver
class CreateBrowser(unittest.TestCase):
    # 初始化
    def setUp(self):  # 调用是自动调用，每一次执行测试用例之前都会调用setUp()
        print('执行之前的操作')
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')


    # 执行测试后的清除工作
    def tearDown(self):  # 调用是自动调用，每一次执行测试用例之后都会调用setUp()
        print('执行之后的操作')
        self.driver.quit()