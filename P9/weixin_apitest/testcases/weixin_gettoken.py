# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 8:20 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : weixin_gettoken.py
# @Software: PyCharm

import requests
import time
import unittest
import requests
import jsonpath
from P9.weixin_apitest.common.unittest_init import Unittest_init
from P9.weixin_apitest.common.ApiDefine import ApiDefine
from P9.weixin_apitest.common.config import Configs

cof = Configs()


class GetToken(Unittest_init):

    def test_gettoken(self):
        '''获取token'''
        kw = {'grant_type': 'client_credential',
              'appid': 'wxb637f897f0bf1f0d',
              'secret': '501123d2d367b109a5cb9a9011d0f084'}
        host = cof.url + "/cgi-bin/token"
        r3 = ApiDefine().gettoken(self.session, url=host, params=kw)
        t = jsonpath.jsonpath(r3.json(), '$.expires_in')[0]
        time.sleep(2)
        self.assertEqual(t, 7200)

    def test_appiderror(self):
        '''appid错误'''
        kw = {'grant_type': 'client_credential',
              'appid': 'wxb637f897f0bf1123123f0d',
              'secret': '501123d2d367b109a5cb9a9011d0f084'}
        host = cof.url + "/cgi-bin/token"
        r3 = ApiDefine().gettoken(self.session, url=host, params=kw)
        t = jsonpath.jsonpath(r3.json(), '$.errcode')[0]
        time.sleep(2)
        self.assertEqual(t, 40013)
