# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 8:32 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : weixin_remarks.py
# @Software: PyCharm
import json

import jsonpath
import requests
from P9.weixin_apitest.common.user_tokens import gettoken, remarks
from P9.weixin_apitest.common.unittest_init import Unittest_init
from P9.weixin_apitest.common.ApiDefine import ApiDefine
from P9.weixin_apitest.common.config import Configs

cof = Configs()


class Remark(Unittest_init):
    access_token = gettoken()
    re = remarks()

    def test_remarks(self):
        '''修改用户列表'''
        self.token = {"access_token": Remark.access_token}
        name = {
            "openid": Remark.re,
            "remark": "lishouwu"
        }
        host = cof.url + '/cgi-bin/user/info/updateremark'
        remarks = ApiDefine().remark(self.session, url=host, params=self.token, data=json.dumps(name))
        self.assertIn("ok", remarks.text)

    def test_f_remarks(self):
        '''修改用户列表,错误token'''
        self.token = {"access_token": 12}
        name = {
            "openid": "ogLL26bESKZ_OVpmIYdL0L9VlZXY",
            "remark": "pangzi"
        }
        host = cof.url + '/cgi-bin/user/info/updateremark'
        remarks = ApiDefine().remark(self.session, url=host, params=self.token, data=json.dumps(name))
        self.assertIn("errcode", remarks.text)
