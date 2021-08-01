'''
@File : user_tokens.py
@Time : 2021/6/30 21:12
@Author: luoman
'''
# import lib
import requests
import jsonpath
from weixin_apitest.common.ApiDefine import ApiDefine

session = requests.Session()

def gettoken():  # 写成一个普通函数--获取token
    kw = {'grant_type': 'client_credential',
          'appid': 'wxb71ae35969722889',
          'secret': '91804f506fe88ec49999a2761743e763'}
    host='https://api.weixin.qq.com/cgi-bin/token'
    r3 = ApiDefine().gettoken(session, host, params=kw)
    assecc_token = jsonpath.jsonpath(r3.json(),'$.access_token')[0]
    return assecc_token





