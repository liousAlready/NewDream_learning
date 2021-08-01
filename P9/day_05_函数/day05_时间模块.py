#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day05_时间模块.py
@time: 2021/4/18 16:14
'''

# 时间： time 和 datetime
import time

# 休眠时间  秒数
# time.sleep(4)

# 格林威治时间（GMT）
# 1.时间元组，即用一个元组装起来的9组数值处理实际那
t1 = (2021, 5, 2, 16, 18, 10, 0, 0, 0)  # 定义时间元组
# 2.时间戳
# 当前时间的时间戳
print(time.time())
# 2.1 把给定的时间元组转换成时间戳
print(time.mktime(t1))
# 2.2 把时间戳转换成时间元组
print(time.localtime(1619943490))
# 3. 格式化显示
# 把写的时间字符串转换成时间元组
print(time.strptime("2021-4-18", "%Y-%m-%d"))
# 把时间元祖转换成自定义的时间字符串
print(time.strftime("2021年4月18", t1))
# 把时间元组转换成自定义的时间字符串
print(time.strftime("%y年%m月%d日", t1))
# 4. 用英文显示时间
print(time.asctime(t1))

import datetime

# 1.时间元组，即用一个元组装起来的9组数值处理实际那
t2 = datetime.datetime(2021, 4, 18, 16, 33, 30, 0)  # 定义时间元组
# 2.截取时间元组中的一部分  年月日
print(t2.year)
print(t2.month)
print(t2.day)
print("========")
print(t2.minute)
print(t2.second)
print("========")

# 获取当前星期几
print(t2.weekday())  # 表示星期一是从0开始
print(t2.isoweekday())  # 表示星期一是从1开始
# 3.获取当前时间
print(datetime.datetime.today())
print(datetime.datetime.now())
# 4.获取时间戳
print(t2.timestamp())  # 把上面的时间元组转换成时间戳
print(t2.fromisoformat(time.strftime("2021-04-18")))  # 把时间字符串转换成实际那
# 5.按照自定义格式
print(t2.strftime("%Y-%m-%d"))  # 把时间元组按照格式输出
# 6.用英文显示时间
print(t2.ctime())
