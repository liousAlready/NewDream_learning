'''
@File : unitest_demo1.py
@Time : 2021/6/27 16:11
@Author: luoman
'''
# import lib

import unittest
import requests
import jsonpath
import time
import json
from weixin_apitest.common.ApiDefine import ApiDefine
from weixin_apitest.common.unittest_init import Unittest_init


from weixin_apitest.common.guanlian import gettoken


class Mytest(Unittest_init):
    access_token = gettoken() # 定义成类属性

    def test_createtag(self):
        '''创建标签'''
        self.token = {
            'access_token':Mytest.access_token}
        tag_name = {"tag": {"name": "150KKk789004"}}
        host = 'https://api.weixin.qq.com/cgi-bin/tags/create'
        r6 = ApiDefine().createtagname(self.session, host, params=self.token,  data=json.dumps(tag_name))
        time.sleep(2)
        print('创建标签', r6.text)

    def test_createtag_30(self):
        '''标签名字长度超过30个字符'''
        self.token = {
            'access_token':Mytest.access_token}
        tag_name = {"tag": {"name": "150KKk8986767"}}
        host = 'https://api.weixin.qq.com/cgi-bin/tags/create'
        r6 = ApiDefine().createtagname(self.session, host, params=self.token,  data=json.dumps(tag_name))

    #@unittest.skipIf(version >=3 , '3以上的版本没有此功能') # 条件成立跳过
    def test_gettag(self):
        '''获取标签'''
        self.token = {
            'access_token': Mytest.access_token}
        host='https://api.weixin.qq.com/cgi-bin/tags/get'
        rtag = ApiDefine().gettagname(self.session,host,params=self.token)
        time.sleep(2)
        print(rtag.text)




