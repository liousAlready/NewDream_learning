'''
@File : baidulink.py
@Time : 2021/5/23 11:26
@Author: luoman
'''
# import lib
from selenium import webdriver
import time
import unittest
# from selenium_demo.comm import createbrowser
from 老师の课堂代码.day12.comm import createbrowser


class TestBaiduLink(createbrowser.CreateBrowser):
    '''百度链接测试用例'''

    def switchwindow(self, linktext):
        self.handle = self.driver.current_window_handle
        self.driver.find_element_by_link_text(linktext).click()
        self.handles = self.driver.window_handles
        for h in self.handles:
            if h != self.handle:
                self.driver.switch_to.window(h)

    # 写测试用例
    def test_news(self):
        '''测试新闻链接'''
        self.switchwindow('新闻')
        time.sleep(3)
        self.assertIn('news', self.driver.current_url)

    def test_hao123(self):
        self.switchwindow('hao123')
        time.sleep(3)
        self.assertIn('hao', self.driver.current_url)

    # @unittest.expectedFailure
    def test_map(self):
        self.switchwindow('地图')
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
