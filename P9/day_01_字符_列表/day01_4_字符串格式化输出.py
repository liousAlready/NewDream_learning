#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day01_4_字符串格式化输出.py
@time: 2021/3/28 15:09
'''

name = "Lily"
age = 19
score = 99.9999
room = 701  # 假设这一栋有10层。 1001 如果崚嶒小于0 左边补0 变成0701

# 按格式出书 Lily今年19岁
# print(name + '今年' + age + '岁') # 错误的输出
# 字符串的格式化输出 % 标识该位置有一个格式化数据
# %s 格式化字符串  %d 格式化十进制数
print("%s今年 %d岁" % (name, age))
# 输出浮点型数据
print("%s今天的考试成绩是%f" % (name, score))
# %.xf  x为想要保存的小数位
print("%s今天的考试成绩是%.4f" % (name, score))
# lily住在701 --lily住在0701号   04补位
print("%s住在%04d号房间" % (name, room))  # 总共要输出4个位置扣款的数据，不够的话 左边补0

# 左右对齐   默认右对齐，左对齐需要加 '-' 号
print('%s住在%-6s号房间' % (name, room))

# 输出lily考试99.99，共展示8个位置，但是左对齐
print('%s')
