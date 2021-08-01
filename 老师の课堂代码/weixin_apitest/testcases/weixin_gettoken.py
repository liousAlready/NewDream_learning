'''
@File : weixin_gettoken.py
@Time : 2021/6/30 20:20
@Author: luoman
'''
# import lib
import unittest
import requests
import jsonpath
class GetToken(unittest.TestCase):
    def setUp(self): # 初始化的，每一个用例在执行的时候，都需要执行setup方法
        self.session = requests.Session()

    def tearDown(self): # 清除资源，每一个用例执行完成后，都需要执行teardown方法
        self.session.close()

    def test_gettoken(self):
        kw = {'grant_type': 'client_credential',
              'appid': 'wxb71ae35969722889',
              'secret': '91804f506fe88ec49999a2761743e763'}
        r3 = requests.get('https://api.weixin.qq.com/cgi-bin/token', params=kw)
        t = jsonpath.jsonpath(r3.json(), '$.expires_in')[0]

        self.assertEqual(t,7200)
    def test_appiderror(self):
        kw = {'grant_type': 'client_credential',
              'appid': 'wxb71ae35969722889999',
              'secret': '91804f506fe88ec49999a2761743e763'}
        r3 = requests.get('https://api.weixin.qq.com/cgi-bin/token', params=kw)
        t = jsonpath.jsonpath(r3.json(), '$.errcode')[0]

        self.assertEqual(t, 40013)