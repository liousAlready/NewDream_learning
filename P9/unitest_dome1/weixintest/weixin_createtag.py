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
import jsonpath
from file.HTMLTestRunner import HTMLTestRunner

version = 3


def gettoken():  # 写成一个普通函数--获取token
    # 微信公众号--获取token--get请求
    kw = {'grant_type': 'client_credential',
          'appid': 'wxb637f897f0bf1f0d',
          'secret': '501123d2d367b109a5cb9a9011d0f084'}
    request = requests.get("https://api.weixin.qq.com/cgi-bin/token", params=kw)
    assecc_token = jsonpath.jsonpath(request.json(), '$.access_token')[0]
    return assecc_token


class Mytest(unittest.TestCase):
    access_token = gettoken()  # 定义成一个类变量

    def setUp(self):  # 初始化，每一个用例在执行的时候，都需要执行setup方法
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    def test_createtag(self):
        '''创建标签'''
        self.token = {
            'access_token': Mytest.access_token}
        tag_name = {"tag": {"name": "150KKk78901234304"}}
        host = 'https://api.weixin.qq.com/cgi-bin/tags/create'
        headers = {'Content-Type': 'application/json'}
        r6 = self.session.post(host, params=self.token, headers=headers, json=tag_name)
        print('创建标签', r6.text)
        self.assertIn('id', r6.text)
        assert 'id' in r6.text, '获取token不成功'

    # @unittest.skip("不需要执行这条用例")
    # @unittest.skipUnless(version < 3, '3以下的版本没有此功能')
    def test_createtag30(self):
        """超过30个字符"""
        self.token = {'assess_token': Mytest.access_token}
        tag_name = {
            "tag": {"name": "asdnmbhasmdhnjkashjdkash djkashnh jkdnjlkasdnjklasbnhdjklashdnjk;ashndjkahzxhjkchjk;asd"}}
        headers = {"Content-Type": "application/json"}
        host = "https://api.weixin.qq.com/cgi-bin/tags/create"
        r6 = self.session.post(host, params=self.token, headers=headers, json=tag_name)
        print('创建标签', r6.content)
        self.assertIn('id', r6.content)
        assert 'id' in r6.content, '获取token不成功'

    # # @unittest.skipIf(version >= 3, '3以上的版本没有此功能')
    # def test_gettag(self):
    #     '''获取标签列表'''
    #     self.token = {'assess_token': Mytest.access_token}
    #     url = 'https://api.weixin.qq.com/cgi-bin/tags/get'
    #     rtag = self.session.get(url, params=self.token)
    #     print (rtag.text)
    #     self.assertIn('tags', rtag.text)


# 使用测试套件-- 控制执行用例的数量，方法有三种：
# 方法一：
suite = unittest.TestSuite()
suite.addTest(Mytest("test_createtag"))
suite.addTest(Mytest("test_gettag"))


# 方法二；把方法一封装到函数
def createsuite():
    suite = unittest.TestSuite()
    suite.addTest(Mytest("test_createtag"))
    return suite


# 方法三：把用例的名字先放到列表中，然后去执行列表
def createtest():
    tests = ['test_createtag', 'test_createtag30', 'test_gettag']
    return unittest.TestSuite(map(Mytest, tests))


#  方法一的执行
# unittest.main(defaultTest='suite')
#  方法二的执行
# unittest.main(defaultTest="createsuite")
#  方法三的执行
# unittest.main(defaultTest='createtest')


now = time.strftime("%Y_%m_%d_%H_%M_%S")
fp = open("/Users/lishouwu/Documents/PycharmProjects/NewDream_learning/P9/unitest_dome1/baogao/" + now + "abc.html,"
                                                                                                         "w+",
          encoding='utf-8')
runner = HTMLTestRunner(stream=fp, title="微信公众号接口报告", description="微信公众号")
runner.run(createtest())
