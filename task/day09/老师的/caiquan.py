'''
@File : caiquan.py
@Time : 2021/5/16 09:41
@Author: luoman
'''
# import lib

import random

class Computer:
    def __init__(self,name):
        self.name = name
        self.score = 0

    def show(self):
        self.cq = random.randint(1, 3)

    # 1—剪刀，2—拳头，3---布
    def pcq(self):
        if self.cq == 1:
            return '剪刀'
        elif self.cq ==2:
            return '拳头'
        elif self.cq ==3:
            return '布'

class Player:
    def __init__(self, name='匿名'):
        self.playername = name
        self.playerscore = 0

    def playershow(self):
        # 用户出拳方式是由用户输入的值
        self.pq = int(input())

    # 1—剪刀，2—拳头，3---布
    def ppq(self):
        if self.pq == 1:
            return '剪刀'
        elif self.pq == 2:
            return '拳头'
        elif self.pq == 3:
            return '布'
        else:
            return '出拳错误'




class StartGame:
     def setcname(self, name):
         if name == 1:
             return '刘备'
         elif name ==2:
             return '孙权'
         elif name == 3:
             return '曹操'
         else:
             return '名字有误'

     def setpname(self):
         name  = input()
         return name

     def cVSp(self,score,playerscore):
         if score ==playerscore:
             print('双方平局')
         else:
             if score > playerscore:
                 print('电脑获胜')
             else:
                 print('玩家获胜')



if  __name__=='__main__':
    s = StartGame()
    print('开始游戏，猜拳开始')
    print('出拳规则:1—剪刀，2—拳头，3---布')
    c = int(input('请输入对方的角色:1—刘备，2—孙权，3—曹操'))
    # 给电脑设置名字
    cname = s.setcname(c)
    computer = Computer(cname)
    print('请输入你的名字')
    pname = s.setpname()
    player = Player(pname)
    print('%s VS %s' % (player.playername,computer.name))
    while True:
        ifstart = input('是否要开始游戏?(y/n)')
        if ifstart != 'n':
             print('请出拳:1—剪刀，2—拳头，3---布,(请输入相对应的数字)')
             player.playershow()
             computer.show()
             print('你出拳:%s' % player.ppq())
             print('%s 出拳：%s' %(cname, computer.pcq()))
             # 判断是出拳的结果
             if player.pq ==1 and computer.cq==3 or \
                player.pq == 2 and computer.cq == 1 or \
                player.pq == 3 and computer.cq == 2:
                 player.playerscore = player.playerscore+1
                 print('%s该局获胜' % pname)
             elif player.pq == 3 and computer.cq == 1 or \
                player.pq == 1 and computer.cq == 2 or \
                player.pq == 2 and computer.cq == 3:
                 print('%s该局获胜' % cname)
                 computer.score = computer.score+1
             else:
                 print('双方平局')
        else:
            print(computer.score, player.playerscore)
            s.cVSp(computer.score, player.playerscore)
            print('结束游戏')
            break




