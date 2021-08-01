# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 6:14 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : dome3.py
# @Software: PyCharm

# 断言
import jsonpath
import requests


# 微信公众号--获取token--get请求
def f3():
    kw = {'grant_type': 'client_credential', 'appid': 'wxb637f897f0bf1f0d',
          'secret': '501123d2d367b109a5cb9a9011d0f084'}
    r3 = requests.get("https://api.weixin.qq.com/cgi-bin/token", params=kw)
    return r3


# assert 表达式1，表达式2
response = f3()
print (response.text)
try:
    assert response.status_code == 200, "断言状态为200失败"
except Exception as e:
    print (e)

assert "expires_in" in response.text, "获取assess_token失败"

# 如果返回的数据是json类型的数据就需要使用jsonpath来取值
# 要把响应的结果转换成json对象，然后通过路径获取json的值
# data = jsonpath.jsonpath(response.json(), "$.expires_in")[0]  # jsonpath.jsonpath()取出来的值是一个列表，需要通过下标来获取数据
# assert data == 7200 , "获取token失败"
# print (data)


# 接口的关联，正则表达式的方法
# 接口关联的第一种方法，使用jsonpath 获取上一个接口的值,作为变量传给下一位
datas = jsonpath.jsonpath(response.json(), "$.access_token")[0]  # jsonpath.jsonpath()取出来的值是一个列表，需要通过下标来获取数据


def f6():
    token = {'assess_token': datas}
    tag_name = {"tag": {"name": "csc21ss"}}
    headers = {"Content-Type": "application/json"}
    host = "https://api.weixin.qq.com/cgi-bin/tags/create"
    r6 = requests.post(host, params=token, headers=headers, json=tag_name)
    return r6


# 接口关联： 方法二--正则表达式进行提取
import re

res = f3()
p = re.compile('"access_token":"(.+?)"')
result = re.findall(p, res.content)
print (result)

# 匹配非数字
str1 = '1231#319003'
p1 = re.compile('1231\D31')
result1 = re.match(p1, str1)
print (result1.group())

# 参数化
# 生成随机整数
import random

i = random.randint(200, 300)  # 包头又包尾
print (i)

# 随机字符串
# 1.定义字符串需要包含的字符
s2 = 'abcdefghilaksjdkzjxlckjASJNDKJANSJ1723123'
j = random.choice(s2)
print (j)
# 2.生成指定长度的随机字符串
s3 = 'abcdefghilaksjdkzjxlckjASJNDKJANSJ1723123'
c = random.sample(s3, 8)
c1 = ''.join(c)
print (c1)

# 方法二
import string

k2 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print (k2)
# 从列表中随机取值
# list1 = ['python', 'java', 'jmeter', 'requests']
# print (random.choice(list1))

# 使用python做参数化
import pymysql

# 建立链接
connection = pymysql.connect(host="192.168.1.9",
                             port=3306,
                             user='windows',
                             password='123456',
                             database='test',
                             charset='utf8',
                             )
# 获取连接的游标
cursor = connection.cursor()
print (cursor)
# sql语句
sql = 'select * from dbshop_user'
# 执行sql语句
cursor.execute(sql)  # 把所有数据存放到游标中
result = cursor.fetchall()  # 取出游标当中的数据
print (result)
# 关闭连接
connection.close()
