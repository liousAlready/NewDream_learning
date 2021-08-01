# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 9:52 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : un_dome1.py
# @Software: PyCharm

'''

unittest执行用例可以用两种环境
1. python 点击菜单上的run 选择要执行的模块名（推荐使用）
2. 使用unittest环境：unittest.模块名.用例

'''
import json
import unittest
import requests
import jsonpath


def gettoken():  # 写成一个普通函数--获取token
    # 微信公众号--获取token--get请求
    kw = {'grant_type': 'client_credential',
          'appid': 'wxb637f897f0bf1f0d',
          'secret': '501123d2d367b109a5cb9a9011d0f084'}
    tokens = requests.get("https://api.weixin.qq.com/cgi-bin/token", params=kw)
    # assecc_token = jsonpath.jsonpath(tokens.json(), '$.access_token')[0]
    # print (assecc_token)
    # return assecc_token
    jsons = json.loads(tokens.text)
    assecc_token = jsons['access_token']
    print (assecc_token)
    return str(assecc_token)


class Mytest(unittest.TestCase):
    access_token = gettoken()  # 定义成一个类变量

    def setUp(self):  # 初始化，每一个用例在执行的时候，都需要执行setup方法
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    def test_createtag(self):
        self.token = {
            'access_token':Mytest.access_token}
        tag_name = {"tag": {"name": "2111232"}}
        host = 'https://api.weixin.qq.com/cgi-bin/tags/create'
        headers = {'Content-Type': 'application/json'}
        r6 = self.session.post(host, params=self.token, headers=headers, json=tag_name)
        print('创建标签', r6.text)
        self.assertIn('id', r6.text)
        assert 'id' in r6.text, '获取token不成功'


unittest.main()
