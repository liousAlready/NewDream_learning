'''
@File : day12_selenium9.py
@Time : 2021/5/23 11:26
@Author: luoman
'''
# import lib
from selenium import webdriver
import time
import unittest
from 老师の课堂代码.baidu_selenium_demo.comm import createbrowser
from selenium.webdriver.common.by import By
from 老师の课堂代码.baidu_selenium_demo.comm.logger import log

class TestBaiduLink(createbrowser.CreateBrowser):
    '''百度链接测试用例'''


    # 写测试用例
    def test_news(self):
        '''测试新闻链接'''
        self.bo.switchwindow(By.LINK_TEXT,'新闻')

        #self.bo.switchwindow(By.LINK_TEXT,'新闻')
        time.sleep(3)
        self.assertIn('news', self.driver.current_url)

    def test_hao123(self):
        self.bo.switchwindow(By.LINK_TEXT, 'hao123')
        time.sleep(3)
        self.assertIn('hao', self.driver.current_url)

    #@unittest.expectedFailure
    def test_map(self):
        self.bo.switchwindow(By.LINK_TEXT, '地图')
        time.sleep(3)
        self.assertIn('map', self.driver.current_url)


if __name__ == '__main__':
    def createsuite():
        # 定义一个测试套件对象
        suite = unittest.TestSuite()
        # 把用例装载到套件中
        suite.addTest(TestBaiduLink('test_map'))

        return suite

    unittest.main(defaultTest='createsuite')


