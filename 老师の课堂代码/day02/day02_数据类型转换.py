'''
@File : day02_数据类型转换.py
@Time : 2021/3/31 20:52
@Author: luoman
'''
# import lib

#类型转换
# 自动转换  强制转换
# 自动转换：发现在数值类型  bool+int+float---float
a = 10
b = True
print(a+b)
c = 3.4
print(a+b+c)
# 强制转换 数据类型的函数进行转换的
print('强制转换成int:', int(a+c))
print('强制转换成int:', int(c))
print('强制转换成float:', float(a))
set1 = {1, 2, 3}
print('强制转换成list:', list(set1))
print('转换成字符串', str(set1))
print('转换成字符串', repr(set1))
str1 = '1+2'
print(str1)
print(eval(str1))
t = 64
print(chr(t))
n = '中'
print('十六进制的形式：%x' % ord(n)) # \u4e2d
tuple1 = (('x', 2), ('y',3))
print(dict(tuple1))







