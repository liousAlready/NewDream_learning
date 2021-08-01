'''
@File : day04-循环语句--for.py
@Time : 2021/4/11 14:06
@Author: luoman
'''
# import lib
'''
for循环语法如下：

for 迭代变量  in  可迭代对象:  # 可迭代对象(序列, 迭代器, 或者是其他支持迭代的对象)
	执行语句... 
[else : 
	执行语句...]
	
每次循环,迭代变量被设置为可迭代对象(序列, 迭代器, 或者是其他支持迭代的对象)的当前元素, 提供执行语句块使用，直到可迭代对象遍历完成终止。

'''
for i in 'hello':
    print(i)


for l in ['a', 'world','python']:
    print(l)

# range([起始值,]结束值[,增量])函数---生成数字序列

for i in range(0, 10, 1):  # 生成的序列:起始值为0，结束值为10(不包含10),每次增量为1
    print(i)

for i in range(1, 10):  # 表示只有起始值和结束值，增量默认为1，生成序列为：1-9，每次增加1
    print(i)

for i in range(10):  # 表示结束值，起始值默认为：0，增量默认为1，生成序列为：0-9，每次增加1
    print(i)

# 使用range() 来遍历列表
list1 = ['world', 'python', 'java']
for i in range(0, len(list1), 1):
    print(list1[i])
# 字典
dict01 = {'name': '小伟', 'age': 20, 'address': 'shanghai'}
for k in dict01.keys():
    print(k)

for v in dict01.values():
    print(v)

# 取出键和值
# 方法一：
for k in dict01.keys():
    print(k, dict01.get(k))  # 通过键获取值

# 方法二：
for k, v in dict01.items():
    print(k, v)

# 举例：使用for循环来计算1--100之间的和
sum = 0
for i in range(1, 101,1):
    sum = sum + i
else:
    print(sum)

## 九九乘法表
print('==============九九乘法表===========')
for i in range(1, 10, 1):
    for j in range(1, i+1, 1):
        print('%d * %d = %d' % (j, i, i*j), end='\t')
    print()

# pass 不执行任何操作，仅起到占位符
for i in range(1,20,2):
    pass
else:
    print('我想输出')



