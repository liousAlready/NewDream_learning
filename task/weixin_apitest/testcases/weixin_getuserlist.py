# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 8:06 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : weixin_getuserlist.py
# @Software: PyCharm


import json
from P9.weixin_apitest.common.ApiDefine import ApiDefine
from P9.weixin_apitest.common.unittest_init import Unittest_init
from P9.weixin_apitest.common.user_tokens import gettoken
import jsonpath
from P9.weixin_apitest.common.config import Configs

cof = Configs()


class Getuserlist(Unittest_init):
    access_token = gettoken()  # 定义成类属性

    def test_getuserlist(self):
        '''获取用户列表'''
        self.token = {
            'access_token': Getuserlist.access_token}
        host = cof.url + '/cgi-bin/user/get'
        userlist = ApiDefine().getuserlist(self.session, host, params=self.token)
        self.assertIn('total', userlist.text)

    def test_f_getuserlist(self):
        '''获取用户列表,token值不对'''
        self.token = {
            'access_token': 12}
        host = cof.url + '/cgi-bin/user/get'
        userlist = ApiDefine().getuserlist(self.session, host, params=self.token)
        self.assertIn("errcode", userlist.text)
