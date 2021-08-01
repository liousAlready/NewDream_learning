#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day04_for循环.py
@time: 2021/4/13 14:20
'''

'''
for循环语法如下：

for 迭代变量 in 可迭代对象： # 可迭代对象（序列、迭代器。或迭代帝乡）
    执行语句...
[else:
    执行语句...]
'''

for i in "hello":
    print(i)

for l in ['a', 'world', 'python']:
    print(l)

# range（起始值,结束值,增量)函数---生成数字序列
print("==============")
for i in range(0, 10, 1):  # 生成序列：起始值：0 结束值：10（包头不包尾） 增量：1
    print(i)
print("======不加增量========")
for i in range(0, 10):  # 只有起始值和结束值，增量默认为1，生成序列为：1-9，每次增加为1
    print(i)
print("======不写起始值========")
for i in range(10):  # 为结束值，起始值默认为0，增量默认为1 生成序列为：1-9
    print(i)

print("======使用range遍历列表========")
# 使用range() 遍历列表
list1 = ['world', 'java', 'python']
for i in range(0, len(list1), 1):  # 取列表数量在进行遍历
    print(list1[i])
print("======使用range遍历字典========")
# 字典
dict01 = {'name': '小薇薇', 'age': 20, 'address': '上海'}
for k in dict01.keys():
    print(k)

for v in dict01.values():
    print(v)
print("======同时取出字典中的键和值========")
# 方法一
# 同时取出键和值
for k in dict01.keys():
    print(k, dict01.get(k))  # 通过键获取值
# 方法二
for k, v in dict01.items():
    print(k, v)

# 举例： 使用for循环来集训1--100的和
sum = 0
for i in range(1, 101, 1):
    sum = sum + i
print(sum)

# 九九乘法表：
print("=====九九乘法表--for循环操作=====")
for i in range(1, 10, 1):
    for j in range(1, i + 1):
        print("%d * %d = %d" % (i, j, i * j), end="\t")
    print()

# pass  不执行任何操作 仅起到占位符
for i in range(1,20,2):
    pass  # 占位符
else:
    print("我草")