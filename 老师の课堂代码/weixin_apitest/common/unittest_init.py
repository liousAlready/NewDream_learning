'''
@File : unittest_init.py
@Time : 2021/6/30 20:57
@Author: luoman
'''
# import lib
import unittest
import requests
class Unittest_init(unittest.TestCase):
    def setUp(self): # 初始化的，每一个用例在执行的时候，都需要执行setup方法
        self.session = requests.Session()

    def tearDown(self): # 清除资源，每一个用例执行完成后，都需要执行teardown方法
        self.session.close()