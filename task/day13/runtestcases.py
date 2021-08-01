#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: runtestcases.py
@time: 2021/5/24 09:34
'''
import unittest
import time
from file.HTMLTestRunner import HTMLTestRunner
from task.day13.comm.config import Config

conf = Config()


def creatsuite_Q():
    suite = unittest.TestSuite()
    casedir = conf.casedir
    dis = unittest.defaultTestLoader.discover(casedir,
                                              pattern='test_*.py',
                                              top_level_dir=None)

    for d in dis:
        for s in d:
            suite.addTests(s)
    return suite


'''
改进测试报告
1.增加测试报告可读性
2.修改测试报告的名字：时间+名字
'''
now = time.strftime("%Y_%m_%d_%H_%M_%S")
filename = "/Users/lishouwu/PycharmProjects/NewDream_learning/task/day13/report/" + now + "_iwebshop.html"
fp = open(filename,
          "w+", encoding="utf-8")
runner = HTMLTestRunner(fp, description="iweb商城测试报告", title="iweb商城测试报告")
runner.run(creatsuite_Q())
