'''
@File : day12_runtestcase.py
@Time : 2021/5/23 11:39
@Author: luoman
'''
# import lib
# 在此文件中把TestBaidu类和TestBaiduLink类中的测试用例在此文件中进行装载并执行
import unittest
# from selenium_demo.testcases.day12_selenium8 import TestBaidu
# from selenium_demo.testcases.day12_selenium9 import TestBaiduLink
from 老师の课堂代码.day12.testcase.day12_selenium8 import TestBaidu
from 老师の课堂代码.day12.testcase.day12_selenium9 import TestBaiduLink


def createsuite():
    # 定义一个测试套件对象
    suite = unittest.TestSuite()
    # 把用例装载到套件中,  此方法有些费时间
    suite.addTest(TestBaidu('test_serch1'))
    suite.addTest(TestBaidu('test_serch2'))
    suite.addTest(TestBaidu('test_serch3'))
    suite.addTest(TestBaidu('test_serch3'))


    suite.addTest(TestBaiduLink('test_map'))
    suite.addTest(TestBaiduLink('test_news'))
    suite.addTest(TestBaiduLink('test_hao123'))

    return suite

# 升级测试用例装载的方法 discover()
# 先定义变量指明用例所在的目录

# 定义函数 使用discover
def creatsuite_B():
    suite = unittest.TestSuite()
    casedir = './testcases/'
    dis = unittest.defaultTestLoader.discover(casedir,
                                              pattern='day12_*.py',
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

unittest.main(defaultTest='creatsuite_B')