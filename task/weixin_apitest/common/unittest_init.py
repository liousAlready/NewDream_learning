# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 8:57 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : unittest_init.py
# @Software: PyCharm
import unittest

import requests


class Unittest_init(unittest.TestCase):

    def setUp(self):  # 初始化，每一个用例在执行的时候，都需要执行setup方法
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()
