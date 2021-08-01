# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 8:43 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : run_all_cases.py
# @Software: PyCharm

from file.HTMLTestRunner import HTMLTestRunner
import unittest
import time
from P9.weixin_apitest.common.config import Configs

cof = Configs()


# 使用discover方法遍历用例
def createSuite():
    testdir = cof.casedir
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(
        start_dir=testdir,
        pattern='weixin_*.py',
        top_level_dir=None
    )

    for d in discover:  # 找用例文件
        # print('d的值', d)
        for j in d:  # 把用例文件里面的用例
            # print('j的值：', j)
            suite.addTests(j)

    return suite


now = time.strftime('%Y_%m_%d_%H_%M_%S')
fp = open(cof.reportpath + now + '_weixin.html',
          'w+', encoding='utf-8')
runner = HTMLTestRunner(stream=fp, title='微信公众号接口报告', description='微信公众号接口报告')
runner.run(createSuite())
