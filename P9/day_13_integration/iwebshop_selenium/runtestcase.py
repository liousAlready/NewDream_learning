#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day12_runtestcase.py
@time: 2021/5/23 11:40
'''

import time
# 在此文件中吧TestBaidu类喝TestBaiduLink类中的测试用例在此文件中进行装载并执行
import unittest
import os
import P9.day_13_integration.iwebshop_selenium.testcase
from P9.day_13_integration.iwebshop_selenium.comm.config import Config
from file.HTMLTestRunner import HTMLTestRunner

conf = Config()


def createsuit():
    # # 定义一个测试套件的对象
    suite = unittest.TestSuite()
    # 把用例装载到套件中，有点费时间
    suite.addTest(P9.day_13_integration.iwebshop_selenium.testcase.baidulink("test_news"))

    return suite


# 升级测试用例装载的方法 discover()
# 先定义变量指明用例所在的目录
casedir = "./testcase"


# 定义函数 使用discover
def createsuite_B():
    suite = unittest.TestSuite()
    dis = unittest.defaultTestLoader.discover(casedir,
                                              pattern="baidu*.py",
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
filename = conf.reportpath + now + "_baidu.html"
if __name__ =="__main__":
    fp = open(filename, "w+", encoding="utf-8")
    runner = HTMLTestRunner(fp, description="百度首页测试报告",
                            title="百度首页测试报告")
    # unittest.main(defaultTest='createsuite_B')
    runner.run(createsuite_B())
