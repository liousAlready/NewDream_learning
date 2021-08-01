# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 4:49 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : weixin_createtag.py
# @Software: PyCharm

'''

unittest执行用例可以用两种环境
1. python 点击菜单上的run 选择要执行的模块名（推荐使用）
2. 使用unittest环境：unittest.模块名.用例

'''
import time
import unittest
import requests
import json
from P9.weixin_apitest.common.ApiDefine import ApiDefine
from P9.weixin_apitest.common.unittest_init import Unittest_init
from P9.weixin_apitest.common.user_tokens import gettoken


class Mytest(Unittest_init):
    access_token = gettoken()  # 定义成类属性

    def test_createtag(self):
        '''创建标签'''
        self.token = {
            'access_token': Mytest.access_token}
        tag_name = {"tag": {"name": "545656"}}
        host = 'https://api.weixin.qq.com/cgi-bin/tags/create'
        r6 = ApiDefine().creatertagname(self.session, host, params=self.token, data=json.dumps(tag_name))
        time.sleep(2)
        print('创建标签', r6.text)

    def test_createtag30(self):
        """超过30个字符"""
        self.token = {'assess_token': Mytest.access_token}
        tag_name = {
            "tag": {"name": "asdnmbhasmdhnjkashjdkash djkashnh jkdnjlkasdnjklasbnhdjklashdnjk;ashndjkahzxhjkchjk;asd"}}
        host = "https://api.weixin.qq.com/cgi-bin/tags/create"
        r6 = ApiDefine().creatertagname(self.session, host, params=self.token, data=json.dumps(tag_name))
        print('创建标签', r6.content)

    def test_gettag(self):
        '''获取标签列表'''
        self.token = {'assess_token': Mytest.access_token}
        url = 'https://api.weixin.qq.com/cgi-bin/tags/get'
        rtag = ApiDefine().gettagname(self.session, url, params=self.token)
        print(rtag.text)
