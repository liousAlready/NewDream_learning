# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 8:20 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : weixin_gettoken.py
# @Software: PyCharm

import unittest
import requests
import json
from P9.weixin_apitest.common.ApiDefine import ApiDefine


class GetToken(unittest.TestCase):

    def setUp(self):  # 初始化，每一个用例在执行的时候，都需要执行setup方法
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    def test_gettoken(self):
        kw = {'grant_type': 'client_credential',
              'appid': 'wxb637f897f0bf1f0d',
              'secret': '501123d2d367b109a5cb9a9011d0f084'}
        r3 = requests.get("https://api.weixin.qq.com/cgi-bin/token", params=kw)
        t = jsonpath.jsonpath(r3.json(), '$.expires_in')[0]

        self.assertEqual(t, 7200)

    def test_appiderror(self):
        kw = {'grant_type': 'client_credential',
              'appid': 'wxb637f897f0bf1f0d',
              'secret': '501123d2d367b109a5cb9a9011d0f084'}
        r3 = requests.get("https://api.weixin.qq.com/cgi-bin/token", params=kw)
        t = jsonpath.jsonpath(r3.json(), '$.errcode')[0]

        self.assertEqual(t, 40013)