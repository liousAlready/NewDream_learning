# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 8:46 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : ApiDefine.py
# @Software: PyCharm

# 把所有接口都应以在这里

class ApiDefine:

    # 获取token
    def gettoken(self, session, url, params):
        responese = session.get(url, params=params)
        return responese

    # 创建用户标签
    def creatertagname(self, session, url, params, data):
        response = session.post(url, params=params, data=data)
        return response

    # 获取用户标签
    def gettagname(self, session, url, params):
        responese = session.get(url, params=params)
        return responese

    # 获取用户列表
    def getuserlist(self, session, url, params):
        response = session.get(url, params=params)
        return response

    # 修改用户备注
    def remark(self, session, url, params, data):
        response = session.post(url=url, params=params, data=data)
        return response
