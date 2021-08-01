'''
@File : day05-时间模块.py
@Time : 2021/4/18 16:13
@Author: luoman
'''
# import lib
# 时间：time 和 datetime
import time
# time.sleep(4) # 程序休眠4S
# 时间戳是指格林威治时间1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒)起至现在的总秒数

# 格林威治时间(GMT)
# 1、时间元组，即用一个元组装起来的9组数字处理时间
t1 = (2021, 5, 2, 16, 18, 10, 0, 0, 0)  # 定义时间元组
# 2、时间戮
# 当前时间的时间戳
print(time.time())
# 2.1 把给定的时间元组转换成时间戳
print(time.mktime(t1))
# 2.2 把时间戳转换成时间元组
print(time.localtime(1619943490))
# 3、格式化显示
# 把写的时间字符串转换时间间元组
print(time.strptime('2021年4月18', '%Y年%m月%d'))
# 把时间元组转换自定义的时间字符串
print(time.strftime('%Y年%m月%d日', t1))

print(time.strftime('%Y-%m-%d %H:%M:%S')) # 默认显示当前的时间
# 4、英文显示时间
print(time.asctime(t1))

import datetime
# 1、时间元组表示：
t2 = datetime.datetime(2021, 4, 18, 16, 32, 30, 0)
# 2、截取时间元组中的部分：
print(t2.year)
print(t2.month)
print(t2.day)
print(t2.weekday())  # 星期一是从0开始
print(t2.isoweekday())  # 星期一是从1开始
# 3、获取当前时间：
print(datetime.datetime.today())
print(datetime.datetime.now())
# 4、获取时间戳：
print(t2.timestamp())  # 把时间元组转换成时间戳
print(t2.fromisoformat('2021-04-18'))  # 把时间字符串转换成时间
# 5、按自定义格式返回字符串
# 把时间元组按格式输出
print(t2.strftime('%Y-%m-%d'))
# 6、用英文显示时间
print(t2.ctime())




