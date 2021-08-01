'''
@File : day01_2_数据类型.py
@Time : 2021/3/28 11:28
@Author: luoman
'''
# import lib
# 数据类型:
'''
1:数字类型 number：整型 int，浮点型 float，布尔型bool，复数类型 complex
2:字符串 str
3:列表 list
4:元组 tuple
5:集合 set
6:字典 dict
'''
# 1、数字类型
# 定义整型
a = 10
# 定义浮点型
b = 1.1
c = 1.1e+2  # 浮点型的科学表示法  1.1e+2 ===1.1*10的2次方 == 110
d = 12677484763  # 1.27e+10
e = 0.000001 # 1.0e-7  1.0*10的-6次方  1*0.000001
# 定义bool类型
f = True  # True--1  False--0
# 复数类型
g = 4.5e-7j

# 如何获取变量的数据类型
print(type(g))
print(type(a))

# 变量占用内存的大小
# 内存溢出的问题  int
import sys
i = 0
j = 10
k = 999999999999
print(sys.getsizeof(i))
print(sys.getsizeof(j))
print(sys.getsizeof(k))
