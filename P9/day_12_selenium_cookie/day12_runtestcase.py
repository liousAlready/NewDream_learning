#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day12_runtestcase.py
@time: 2021/5/23 11:40
'''

# 在此文件中吧TestBaidu类喝TestBaiduLink类中的测试用例在此文件中进行装载并执行
import unittest
from P9.day_12_selenium_cookie.testcase.day12_selenium8_unitest import TestBaidu
from P9.day_12_selenium_cookie.testcase.day12_selenium9 import TestLink
from file.HTMLTestRunner import HTMLTestRunner
import time


def createsuit():
    # # 定义一个测试套件的对象
    suite = unittest.TestSuite()
    # 把用例装载到套件中，有点费时间
    suite.addTest(TestBaidu('test_serch1'))
    suite.addTest(TestBaidu('test_serch2'))
    suite.addTest(TestBaidu('test_serch3'))
    suite.addTest(TestLink('test_news'))
    suite.addTest(TestLink('test_hao123'))
    suite.addTest(TestLink('test_map'))
    return suite


# 升级测试用例装载的方法 discover()
# 先定义变量指明用例所在的目录
casedir = "./testcase"


# 定义函数 使用discover
def createsuite_B():
    suite = unittest.TestSuite()
    dis = unittest.defaultTestLoader.discover(casedir,
                                              pattern="day12_*.py",
                                              top_level_dir=None)
    '''
    file1：
        三个用例
    file2：
        四个用例
    '''
    for d in dis:  # 遍历文件
        for s in d:  # 遍历每个文件中的用例
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
filename = "/Users/lishouwu/PycharmProjects/NewDream_learning/P9/file/" + now + "_baidu.html"
# if __name__ =="__main__":
fp = open(filename,
          "w+", encoding="utf-8")
runner = HTMLTestRunner(fp, description="百度首页测试报告",
                        title="百度首页测试报告")
# unittest.main(defaultTest='createsuite_B')
runner.run(createsuite_B())
