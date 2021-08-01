'''
@File : day04-函数.py
@Time : 2021/4/11 15:07
@Author: luoman
'''
# import lib

'''
定义函数语法：
def function(params):
    block
return expression/value

数学函数：
f(x)=2x+1
'''
def f(x):
    s = 2*x+1
    return s  # 可以改写: return 2*x+1

# 函数定义完成后，需要被使用才能实现其功能
# 假设x=1
c = f(1)
print('函数的运行结果是：', c)

'''
假设定义数学函数：
f1(x,y)= x*y+2*x+1  二元一次函数
f1(2,4)= 2*4+2*2+1 = 13
'''
def f1(x, y):
    return  x * y + 2 * x + 1

d = f1(2, 4)
print('f1的结果是', d)
'''
f2(x,y,z) = x+y+z+10
f2(3,4,5) = 3+4+5+10=22
'''
def f2(x, y, z):
    return x+y+z+10

e = f2(3, 4, 5)
print('f2的结果是', e)

# python中是可以存在没有参数和没有返回值的函数的
def f3():
    print('$')

f3()
# 可能是有参数但没有返回值  以下是错误示范
# def f4(n):
#    return print('$'*n) # print() 没有返回值，所以不能在前面写 return

# f =f4(4)
# print('f4的运行结果是:', f)
def f4(n):
    return '$'*n

f = f4(4)
print('f4的运行结果是:', f)
# 把定义函数的时候使用的参数称之为 形式参数---形参
# 把调用函数的时候使用的具体值称之为 实际参数---实参

# 参数传递：传数值  传地址
# 可变的数据类型：列表，字典 -- 传地址
# 不可变的数据类型：数值类型，字符串，元组，集合  -- 传数值
a = 10
b =5
def f5(a, b):
    a = a + b

    return a
f5(a,b)
print('a的值是:', a)


list01 = ['nn', 'java']
def f6(list, s):
    list.append(s)
    return list

f6(list01,'hello')

list02 = list01








