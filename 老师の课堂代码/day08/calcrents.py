'''
@File : calcrents.py
@Time : 2021/5/9 09:09
@Author: luoman
'''
# import lib
from demo.car import Car, Bus, PiCar, Truck

def carfactory():
    a = Bus('A', 800, 5)
    b = Bus('B', 400, 5)
    c = Bus('C', 800, 5)
    d = Bus('D', 1300, 51)
    e = Bus('E', 1500, 55)
    f = PiCar('F', 500, 5, 0.45)
    g = PiCar('G', 450, 5, 2.0)
    h = Truck('H',200,3)
    i = Truck('I', 1500, 25)
    j = Truck('J', 2000, 35)

    carlist = [a, b, c, d, e, f, g, h, i, j]


    return carlist


def calcmoney(count,index,days):
    clist = carfactory()

    for c in range(1,len(clist)+1):
        if index == c:
            if 1<=index<=5: # 表示租客车
                allpeople = count * clist[index-1].peoplecount
                allrents  = count * days * clist[index-1].rents
                return '%-10d' % allpeople + '0.00'+'%10d'%allrents
            elif 6<=index<=7:
                allpeople = count * clist[index - 1].peoplecount
                allrents = count * days * clist[index - 1].rents
                loads = count *clist[index-1].goods
                return '%-10d' % allpeople + '%.2f'%loads+'%10d'%allrents
            else:
                allrents = count * days * clist[index - 1].rents
                loads = count * clist[index - 1].goods
                return  '0' + '%10.2f'% loads+'%10d'%allrents
        else:
             continue

def testcar():
    print('欢迎使用嗒嗒租车系统，请尝试租车(1--租车,0--不租车)')
    i = int(input())
    if i==0 or i==1:
        if i ==1:
            print('我们有以下车型：')
            print('''序号     名称     载客量      载货量        租金
                 （人）     （吨）    （元/天）''')
            for i in range(1, len(carfactory())+1, 1): # 显示车型
                print(i, carfactory()[i-1])

            c = int(input('请输入租车的数量:'))

            m = int(input('请输入租车的天数:'))
            n = int(input('请输入车的序号:'))
            if 1<=n<=10:
                s= calcmoney(c,n,m)
                print(s)
            else:
                print('输入有误')

        else:
            print('0  0.0  0')
    else:
        print('输入有误')

# 启动程序
testcar()
