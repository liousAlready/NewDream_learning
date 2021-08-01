'''
@File : day12_runtestcase.py
@Time : 2021/5/23 11:39
@Author: luoman
'''
# import lib
# 在此文件中把TestBaidu类和TestBaiduLink类中的测试用例在此文件中进行装载并执行
import unittest
from file.HTMLTestRunner import HTMLTestRunner
from 老师の课堂代码.baidu_selenium_demo.comm.emailUtils import sendemail

import time
from 老师の课堂代码.baidu_selenium_demo.comm.config import Config
conf = Config()
def creatsuite():
    suite = unittest.TestSuite()
    casedir = './testcases/'
    dis = unittest.defaultTestLoader.discover(casedir,
                                              pattern='baidu*.py',
                                              top_level_dir='./testcases/')

    for d in dis:  # 遍历文件的
        for s in d:  # 遍历每一个文件中的用例
            suite.addTests(s)

    return suite



now = time.strftime('%Y_%m_%d_%H_%M_%S')
filename = conf.reportpath+now+'_baidu.html'

fp = open(filename,
          'w+', encoding='utf-8')

runner = HTMLTestRunner(stream=fp,
                                       description='百度首页测试报告',
                                       title='百度首页测试报告')


runner.run(creatsuite())

sendemail(filename)
#unittest.main(defaultTest='creatsuite_B')
