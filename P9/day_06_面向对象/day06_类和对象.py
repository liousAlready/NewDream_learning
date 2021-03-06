#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day06_类和对象.py
@time: 2021/4/21 20:49
'''

'''
面向过程：C愚园，把要实现的功能 按流程一步一步的来实现
比如：美团点歌外卖：先要打开美团，选择商家，选择外面，商家截单，骑手送餐，拿到外卖
面向对象：对象
比如：美团点外卖：涉及到哪些对象？  美团软件。商家接单，骑手送外卖，你吃东西
'''

# 面对对象包括三个过程：面向对象分析（00A）、面向对象设计(00D)、面向对象编程(00p)
'''
描述对象：属性/特效  操作/方法
把具有相同属性或者方法的对象进行抽象--总结为一个类
类：类是对象的抽象，是一个抽象的概念
对象：对象是类的具体化
'''

# 一定是先设计好类，才能有对象
''''
定义类的语法：
class 类名：  # 首字母一定要大写
    属性(变量）
        分类：类属性，实例属性（对象属性），内置属性
        实例属性（对象属性）：定义在含有形式参数中含有  self参数的函数中，必须是 self.属性名
        内置属性：是由系统定义的，只需要会用就行，一定是双 __ 开头或者结尾 
    方法（函数）

'''


class Qishou:
    ''' 这是定义的一个骑手类 '''
    name = '骑手'  # 类属性：可以被类名引用，也可以被对象引用： 所有对象都拥有的属性且属性的值相同，定义成类属性
    majia = '黄色'  # 所有的骑手都拥有黄色的马甲  所以可以定义成类属性

    def __init__(self, phone, address):  # 实例属性
        self.phone = phone  # "13677484764"
        self.address = address  # "湖南长沙"

    def postwaimai(self):  # 方法
        print("送外卖！")
        self.t = "21:26"  # 实例属性： 所有对象都应该有的属性，但是每个对象的属性值 都不相同


# 定义对象
# 对象 = 类名([参数])
Q1 = Qishou(1929213123, "网吧")
# 获取对象的属性 ：  对象名.属性
print(Q1.phone)  # 实例 可以应用类属性
print(Q1.address)
print(Q1.name)
print(Qishou.name)  # 类属性 可以被类名引用 也可以被对象引用
# 获取对象的方法： 对象名.方法
Q1.postwaimai()

# 内置函数
print(Qishou.__doc__)  # 类的文档属性

# 创建第二个骑手
Q2 = Qishou("177688521", "jjj")
print(Q2.phone)
print(Q2.address)
