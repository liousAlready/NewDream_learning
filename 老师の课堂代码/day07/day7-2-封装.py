'''
@File : day7-2.py
@Time : 2021/4/28 20:55
@Author: luoman
'''
# import lib
# 面向对象编程三大特性: 封装，继承，多态
# 同一个项目肯定不是一个人开发的，如何节省时间，如何减少维护的成本
# 实现与使用分离，高内聚 低耦合

'''
封装：
   原因：1、保护代码安全：不希望实例属性在外部被修改或者直接引用，要求把实例属性改成私有实例属性
            需要通过公共的实例方法进行引用
            也可以把方法封装成私有方法，只能在类的内部使用，类的外部是不能直接使用
        2、降低代码的复杂程度
'''
class Qishou:
    name = '美团骑手'

    @classmethod
    def talk(cls):
        print('您好，您的外卖到了！！')
        cls.name = '美团小帮手'

    @classmethod
    def good(cls):
        print('记得五星好评！！')

    @staticmethod
    def songcan():  # 不带self 和 cls
        print('已经开始送餐了！！')


    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def getname(self, s):  # 获取私有属性的值
        if s == '经理':
            return self.__name
        else:
            return '没有权限'

    def setname(self, name, phone):  # 对私有属性进行赋值
        if self.__phone == phone:
           self.__name = name


    def __showaddress(self):
        print('%s,请问你在哪里'% self.__name)

    def __isplay(self):
        print('%s是否达到' % self.__name)

    def showqishou(self):
        self.__showaddress()
        self.__isplay()


    def __str__(self):
        return '我是%s,我的联系方式是%s' % (self.__name, self.__phone)



q1 = Qishou('张三', '13589897878')

q1.setname('张小三', '13589897800')
print(q1.getname('经理'))

q1.showqishou()