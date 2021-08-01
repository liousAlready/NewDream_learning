'''
@File : run_all_cases.py
@Time : 2021/6/30 20:43
@Author: luoman
'''
# import lib
# import lib
import unittest
import HTMLTestRunner
# 使用discover方法遍历用例
def createSuite():
    testdir=  '/Users/luoman/python_code/p9_code/weixin_apitest/testcases/'
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(
        start_dir=testdir,
        pattern='weixin_*.py',
        top_level_dir=None
    )

    for d in discover:  # 找用例文件
        print('d的值', d)
        for j in d:  # 把用例文件里面的用例
            print('j的值：', j)
            suite.addTests(j)

    return suite

import time
now = time.strftime('%Y_%m_%d_%H_%M_%S')
fp = open('/Users/luoman/python_code/p9_code/weixin_apitest/reports/'+now+'_weixin.html',
          'w+',encoding='utf-8')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='微信公众号接口报告',description='微信公众号接口报告')
runner.run(createSuite())