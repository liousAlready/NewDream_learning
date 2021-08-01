#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: first_air.py
@time: 2021/4/29 13:45
'''

'''

1.士兵瑞恩有一把AK47
2.士兵可以开火(士兵开火扣动的是扳机)
3.枪 能够 发射子弹(把子弹发射出去)
4.枪 能够 装填子弹 --增加子弹的数量
Soldier        Gun
---------      ------------
name            model
gun             bullet_count
----------     -------------
__init__(self) __init__(self)
fire(self)     add_bullet(self,count)
               shoot(self)
————————————————
版权声明：本文为CSDN博主「yangkaiorange」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/yangkaiorange/article/details/82461496

'''


class Solodier:

    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun == None:
            print("%s 还没有获取武器呢" % self.name)
            return
        print("%s 大喊道：冲啊" % self.name)
        self.gun.add_bullet(50)
        self.gun.shoot()


class Gun:

    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    # 只要子弹的数量足够，就能发射，所有shoot方法不需要传递参数
    def shoot(self):
        # 判断子弹的数量
        if self.bullet_count <= 0:
            print("你的%s已经没有子弹了，请尽快补充弹药" % self.model)
            return
        self.bullet_count -= 3
        print("%s 突突突... %d" % (self.model, self.bullet_count))


ak = Gun("AK-47")
na = Solodier("大兵子")
na.gun = ak
na.fire()
