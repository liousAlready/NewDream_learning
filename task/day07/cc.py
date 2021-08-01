#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: cc.py
@time: 2021/5/8 13:28
'''


import decimal
class Car:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z


if __name__ == '__main__':
    list=[]
    c = Car(5,0,800)
    list.append(c)

    c=Car(5,0,400)
    list.append(c)

    c = Car(5, 0, 800)
    list.append(c)

    c = Car(51, 0, 1300)
    list.append(c)

    c = Car(55, 0, 1500)
    list.append(c)

    c = Car(5,0.45, 500)
    list.append(c)

    c = Car(5, 2.0, 450)
    list.append(c)

    c = Car(0, 3, 200)
    list.append(c)

    c = Car(0,25,1500)
    list.append(c)

    c = Car(0, 35, 2000)
    list.append(c)

    while True:
        x = int(input())
        if x == 0:
            print('0 0.00 0')
            break
        else:
            x = 0
            y=0
            z=0
            n = int(input())
            for i in range(0,n):
                a,b = input().split(' ')
                a = int(a)
                b = int(b)
                x = x + (list[a-1].getX() * b)
                y = y + (list[a-1].getY() * b)
                z = z + (list[a-1].getZ() * b)

            print(x,'%.2f'%y,z)

