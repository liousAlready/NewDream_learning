'''
@File : ApiDefine.py
@Time : 2021/6/30 20:45
@Author: luoman
'''
# import lib

# 把所的接口都定义在这里
class ApiDefine:
    # 获取token接口
    def gettoken(self, session, url, params):
        response = session.get(url, params=params)
        return response
    # 创建用户标签
    def createtagname(self,session,url,params, data):
        response = session.post(url, params=params,data=data)
        return response

    # 获取用户标签
    def gettagname(self,session, url, params):
        response = session.get(url, params=params)
        return response