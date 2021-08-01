'''
@File : day05-函数的递归.py
@Time : 2021/4/18 11:02
@Author: luoman
'''
# import lib
# 函数自己调用自己--函数的递归
def story():
    print('曾经有座山，山里有座庙，庙有一个老和尚和小和尚，老和尚给小和尚讲故事，讲的故事是:')
    story()

# story()
# 通过循环进行1--100的加法运算
sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)

# 改进成递归
def add(n): # n --100, 99,98...1
    if n == 1:
        return 1  #add(1) =1
    else:
        return add(n-1) + n  # 100--- add(99)      +100
                              #           |
                             # 99 --- add(98) +99  +100
                            #             |
                             # 98 --- add(97) +98  +99 +100

                            #  2  ---- add(1)+ 2 +3 +3+4+5+...+99+100

                          #  结果  ---- 1+ 2 +3 +3+4+5+...+99+100

s = add(100)
print(s)

# 匿名函数：函数的定义不需要写 def 关键字，也不需要return关键字  ----lambda
# 有些函数的功能只有一句话就可以进行实现
#

# 转换成匿名函数
sum = lambda a, b : a+b  # 此时的:号前的a,b 就是函数的形式参数，sum既可以保存函数的运算结果，也可以当作函数的名字
print(sum(3, 4))
# 使用匿名函数来比较两个数的大小
m = lambda : 4 if 4 > 5 else 5
print(m())

#  内置函数---有些函数是由系统定义好的

# 定义函数的时候：1、除特殊情况外，自定义函数中不写input语句和print语句
#              2、定义函数的时，要注意函数的名字不能与内置函数相同


# def print(a,b):
#     return a+b
# print(print(12,34))
# i = 10
# j = 20
# print(print(i, j))


