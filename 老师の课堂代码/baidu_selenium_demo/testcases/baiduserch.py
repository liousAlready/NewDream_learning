'''
@File : day12_selenium8.py
@Time : 2021/5/23 09:37
@Author: luoman
'''
# import lib

import time

from 老师の课堂代码.baidu_selenium_demo.comm import createbrowser

class TestBaidu(createbrowser.CreateBrowser):
    '''百度搜索测试用例'''
    # def __init__(self):
    #     self.kw = self.driver.find_element_by_id('kw')
    #     self.su = self.driver.find_element_by_id('su')

    def serch(self, keyword):
        self.driver.find_element_by_id('kw').send_keys(keyword)
        self.driver.find_element_by_id('su').click()


    # 写测试用例
    def test_serch1(self):
        '''测试正常关键字的用例'''
        self.serch('python')

        time.sleep(3)
        self.assertIn('python', self.driver.title)

    def test_serch2(self):
        '''测试包含特殊符号的用例'''
        self.serch('python??')
        self.driver.find_element_by_id('kw').send_keys('python?')

        time.sleep(3)
        self.assertIn('python', self.driver.title)


    def test_serch3(self):
        '''测试不输入关键字的测试例'''
        self.serch('')
        self.driver.find_element_by_id('kw').send_keys('')
        time.sleep(3)
        self.assertIn('百度一下', self.driver.title)


