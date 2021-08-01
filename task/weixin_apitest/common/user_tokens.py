# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 2:22 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : user_tokens.py
# @Software: PyCharm

import requests
from P9.weixin_apitest.common.ApiDefine import ApiDefine
from P9.weixin_apitest.common.config import Configs
import jsonpath
from P9.weixin_apitest.common.config import Configs

session = requests.Session()

cof = Configs()


def gettoken():
    kw = {'grant_type': 'client_credential',
          'appid': 'wxb637f897f0bf1f0d',
          'secret': '501123d2d367b109a5cb9a9011d0f084'
          }
    host = cof.url + "/cgi-bin/token"
    r3 = ApiDefine().gettoken(session, host, params=kw)
    access_token = jsonpath.jsonpath(r3.json(), '$.access_token')[0]
    # print(access_token)
    return access_token


def remarks():
    '''获取用户列表'''
    token = {
        'access_token': gettoken()
    }
    host = cof.url + '/cgi-bin/user/get'
    userlist = ApiDefine().getuserlist(session, host, params=token)
    user = jsonpath.jsonpath(userlist.json(), '$.data.openid[0]')
    # print(user[0])
    return user[0]
