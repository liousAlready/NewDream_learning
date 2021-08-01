#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day07_构造方法.py
@time: 2021/4/28 20:10
'''

'''
构造方法 __init__() 属于构造方法，初始化对象，给对象申请内存，构造方法可以与参数，也可以没有参数

self ： 表示的是类的实例  是不需要传值的，系统自动传入实例给self

实例方法：所有的实例方法一定有参数self
     可以使用[实例]进行调用，但是不能用[类名]进行调用
     作用：如果每一个实例（对象）使用该方法都带有自己的特征的时候，就需要使用实例方法
          如果需要实例属性进行修改，也要使用实例方法
          
类方法：所有类的方法前面必须要有 装饰器 @classmethod 而且必须有参数cls，用来传类名
    调用：可以使用实例调用
         也可以使用类名进行调用
    类方法作用：对类属性进行修改
          
静态方法：所有的静态方法的前面都必须要有装饰器 @staticmethod
    调用：可以使用实例调用
         也可以使用类名进行调用
    作用：如果所有对象的操作都是相同的，没有任何区别 
    
内置方法：
    特点：以 __开头和结尾，不需要自己定义，可以直接使用，也可以重新定义
    __del__(self):释放内存

'''


'''
构造方法 __init__() 属于构造方法，初始化对象，给对象申请内存，构造方法可以与参数，也可以没有参数
'''


class Qishou:
    name = "美团骑手"

    @classmethod
    def talk(cls):  # 定义了一个类方法   cls <= class
        print("您好，您的外卖到了")
        cls.name = "美团小帮手"  # 对类属性进行修改

    @classmethod
    def good(cls):  # 定义了一个类方法
        print("记得五星好评哦~")

    @staticmethod
    def songcan():  # 定义了一个静态方法
        print("已经开始配送了！")

    def __init__(self, name, phone):  # 每个对象在初始化的时候 需要不同的值 就需要构造方法
        print("我是构造方法")
        self.name = name
        self.phone = phone


    def shouaddress(self):
        print("%s 你在哪里" % self.name)

    def __del__(self):
        print("我执行完了，要被释放资源了")


    def __str__(self): # 假设实例输出的格式是：我是xxx，我的联系方式是xxx
        return '我是%s。我的联系方式是%s' % (self.name,self.phone)


q1 = Qishou("张三", 1557282821)  # 创建对象的时候，就自动调用构造方法，通过类名

print(q1.name)  # 通过传入参数  再调用实例化属性
print(q1.phone)
# 修改初始值为张三丰
q1.name = "张三丰"
print(q1.name)
# 只有一个self的时候，可以直接调用这个方法不需要添加参数
q1.shouaddress()


'''
self ： 表示的是类的实例  是不需要传值的，系统自动传入实例给self
'''

# 如果自己不写构造方法，系统会提供一个空的构造方法
class Beizi:
    def bbb(self):
        print("杯子的颜色是红色")


b = Beizi()
b.bbb()

'''
实例方法：所有的实例方法一定有参数self
     可以使用[实例]进行调用，但是不能用[类名]进行调用
     作用：如果每一个实例（对象）使用该方法都带有自己的特征的时候，就需要使用实例方法
          如果需要实例属性进行修改，也要使用实例方法
'''
# 错误方法
# Qishou.shouaddress()
q2 = Qishou("网肖王",1555282813123)
q2.shouaddress()

'''
类方法：所有类的方法前面必须要有 装饰器 @classmethod 而且必须有参数cls，用来传类名
    调用：可以使用实例调用
         也可以使用类名进行调用
    类方法作用：对类属性进行修改 
'''
q1.talk()  # 使用实例进行调用
Qishou.good()  # 使用类名进行调用
print(Qishou.name)

'''
静态方法：所有的静态方法的前面都必须要有装饰器 @staticmethod
    调用：可以使用实例调用
         也可以使用类名进行调用
    作用：如果所有对象的操作都是相同的，没有任何区别 
'''
q1.songcan() # 使用实例进行调用
Qishou.songcan()   # 使用类名进行调用

'''
内置方法：
    特点：以 __开头和结尾，不需要自己定义，可以直接使用，也可以重新定义
    __del__(self):  析构方法：释放内存
    def __del__(self):
        print("我执行完了，要被释放资源了")
'''

# str
print(q1)
print(q2)