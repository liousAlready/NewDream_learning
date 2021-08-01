'''
@File : car.py
@Time : 2021/5/9 08:58
@Author: luoman
'''
# import lib

class Car:
     def __init__(self, carname, rents):
         self.carname = carname
         self.rents = rents


class Bus(Car):
     def __init__(self,carname,rents, peoplecount):
         self.peoplecount = peoplecount
         Car.__init__(self, carname, rents)

     def __str__(self):
         return '%5s'%self.carname + '%12d'%self.peoplecount +'%24d'%self.rents


class Truck(Car):
     def __init__(self,carname,rents,goods):
         self.goods = goods
         Car.__init__(self, carname, rents)




     def __str__(self):
         return '%5s'%self.carname + '%25.2f'%self.goods + '%10d'%self.rents


class PiCar(Car):
     def __init__(self,carname,rents,peoplecount,goods):
         self.goods = goods
         self.peoplecount = peoplecount
         Car.__init__(self, carname, rents)

     def __str__(self):
         return '%5s'%self.carname + '%12d'%self.peoplecount + '%13.2f'%self.goods + '%10d'%self.rents
