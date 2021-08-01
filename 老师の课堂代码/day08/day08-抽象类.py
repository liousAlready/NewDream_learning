'''
@File : day08-抽象类.py
@Time : 2021/5/9 10:23
@Author: luoman
'''
# import lib

# 抽象类：把类再次进行抽象
# 抽象类中要包含抽象方法：只有定义没有方法体的方法，由子类来具体实现这个方法
# 抽象类要实现就一定会有继承

import abc
class People(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_name(self):
        pass

class Student(People):
    def set_name(self, name):                #参数个数不同
        print('Student,set_name = %s' % name)


s= Student()
s.set_name('张三')


# car 类---具体显示车的载人量，载货量，租金
# 载人量，载货量，租金 是由各子类具体实现的
import abc
class Car(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calc(self):
        pass

    def show(self):
        print(self.calc())

class Picar(Car):
    def calc(self):
        return '人数' + '+ 租金' + '货物量'


class Bus(Car):
    def calc(self):
        return '人数'+'+ 租金'


c1 = Bus()
c1.show()

c2 = Picar()
c2.show()



class ShowPayResult(metaclass=abc.ABCMeta):  # 前端
    @abc.abstractmethod
    def qudao(self):
        pass
    def presult(self):
        print('收钱包到账:', self.qudao(200))


class weixin(ShowPayResult):# 后端
    def qudao(self, money):
        return '%s' % '微信支付'+'%d' % (money+2)

class zhifubao(ShowPayResult):
    def qudao(self, money):
        return '%s' % '支付宝支付'+'%d' % money


w = weixin()

w.presult()

z = zhifubao()
z.presult()
