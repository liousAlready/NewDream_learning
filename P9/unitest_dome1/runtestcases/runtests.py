# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 8:25 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : runtests.py
# @Software: PyCharm

import unittest
from file.HTMLTestRunner import HTMLTestRunner
import time
import io

# 使用discover方法遍历用例
def createSuit():
    testdir = "/Users/lishouwu/Documents/PycharmProjects/NewDream_learning/P9/unitest_dome1/weixintest"
    suite = unittest.TestSuite()
    discover = unittest.TestLoader.discover(
        start_dir=testdir,
        pattern='weinxin_*.py',
        top_level_dir=None
    )

    for d in discover:
        for j in d:
            suite.addTests(j)
    return suite

now = time.strftime("%Y_%m_%d_%H_%M_%S")
fp = io.open("/Users/lishouwu/Documents/PycharmProjects/NewDream_learning/P9/unitest_dome1/baogao/" + now + "abc.html,",
             "w+",encoding="utf-8")
runner = HTMLTestRunner(stream=fp, title="微信公众号接口报告", description="微信公众号")
runner.run(createSuit())
