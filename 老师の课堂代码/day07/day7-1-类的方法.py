'''
@File : day7-1.py
@Time : 2021/4/28 20:10
@Author: luoman
'''
# import lib
'''

1：构造方法: __init__(),初始化对象，给对象申请内存，构造方法可以有参数，也可以没有参数
 如果自己不写构造方法，系统会提供一个空的构造方法

2：self:表示的是类的实例，是不需要传值，系统自己传入实例给self

3：实例方法：所有的实例方法一定会有参数self
      可以使用[实例]进行调用，但是不能用[类名]进行调用
      作用：如果每一个对象(实例),使用该方法都带有自己的特征的时候
           如果需要实例属性进行修改，也要使用实例方法
      
4: 类方法： 所有类的方法前面必须要有装饰器 @classmethod ，而且必须有参数 cls,用来传类名
      调用：可以使用实例进行调用
           也可以使用类名进行调用
      类方法作用：对类属性进行修改
      
5: 静态方法：所有的静态方法前面都必须要装饰器 @staticmethod
      调用：可以使用实例进行调用
           也可以使用类名进行调用
      作用：如果所有对象的操作都是相同的，没有任何区别  
6、内置方法：
      特点：以__开头和结尾，不需要自己定义，可以直接被系统调用，也可以重新定义
           __del__(self)：析构方法：释放资源
           __str__(self,…)：自定义实例输出方法，写好该方法后，替换实例默认的输出操作          
'''
class Qishou:
    name = '美团骑手'

    @classmethod
    def talk(cls):  # 定义了一个类方法，cls <= class
        print('您好，您的外卖到了！！')
        cls.name = '美团小帮手'

    @classmethod
    def good(cls):
        print('记得五星好评！！')

    @staticmethod
    def songcan():  # 不带self 和 cls
        print('已经开始送餐了！！')


    def __init__(self, name, phone): # 每个对象在初始化的时候需要不同的值就需要使用构造方法
        print('我是构造方法')
        self.name = name
        self.phone = phone

    def showaddress(self):
        print('%s在哪里'% self.name)

    def __del__(self):
        print('我执行完了，要被释放资源了')

    def __str__(self):  # 假设实例输出的格式是: 我是XXX，我的联系方式是XXX
        return '我是%s,我的联系方式是%s' % (self.name, self.phone)





q1 = Qishou('张三', '13589897878')  # 创建对象的时候，就自动调用构造方法，通过类名
print(q1.name)
q1.name = '张小三'
print(q1.name)
q1.showaddress()
q2 = Qishou('王小五', '134567878676')
q2.showaddress()
# Qishou.showaddress() 错误案例
q1.talk()
Qishou.good()
print(Qishou.name)

q1.songcan()
Qishou.songcan()

print(q1)  # 打印对象的时候，默认输出 ：<__main__.Qishou object at 0x1020632b0> --对象所在内存的地址
print(q2)

'''
class Beizi:

    def bbb(self):
        print('杯子的颜色是红的')

bb = Beizi()

bb.bbb()
'''
#