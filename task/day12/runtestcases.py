#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: runtestcases.py
@time: 2021/5/24 09:34
'''

import unittest
from task.day12.testcases.test_true import TestAdd
from task.day12.testcases.test_false import TestLogin
import time
from file.HTMLTestRunner import HTMLTestRunner


def creatsuit():
    # suite = unittest.TestSuite()
    # # test_true
    # suite.addTest(TestAdd('test_Loingt'))
    # suite.addTest(TestAdd('test_addcart'))
    # suite.addTest(TestAdd('test_paycart'))
    # suite.addTest(TestAdd('test_quejiesuan'))
    # suite.addTest(TestAdd('test_address'))
    # suite.addTest(TestAdd('test_png'))
    # # test_false
    # suite.addTest(TestLogin('test_loginf'))
    # suite.addTest(TestLogin('test_loginf1'))
    # return suite

    suite=unittest.TestSuite()
    loader=unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestAdd,TestLogin))  #测试用例类名直接传入


# 定义函数 使用discover
def creatsuite_Q():
    suite = unittest.TestSuite()
    casedir = './testcases/'
    dis = unittest.defaultTestLoader.discover(casedir,
                                              pattern='test_*.py',
                                              top_level_dir=None)
    '''
    file1:
        三个用例
    file2:
        四个用例

    '''
    for d in dis:
        for s in d:
            suite.addTests(s)
    return suite

# HTMLTestRunnaer 模块生成测试报告
# 存放的位置：将该文件保存在python的lib文件当中
'''
改进测试报告
1.增加测试报告可读性
2.修改测试报告的名字：时间+名字
'''
now = time.strftime("%Y_%m_%d_%H_%M_%S")
filename = "/Users/lishouwu/PycharmProjects/NewDream_learning/task/day12_" + now + "_baidu.html"
fp = open(filename,
          "w+", encoding="utf-8")
runner = HTMLTestRunner(fp, description="iweb商城测试报告",title="iweb商城测试报告")
runner.run(creatsuite_Q())

