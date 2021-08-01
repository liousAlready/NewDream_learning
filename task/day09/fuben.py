#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day09.py
@time: 2021/5/13 09:16
'''

import random


class Computer:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def computer_name(self, number):
        self.number = number
        if number == 1:
            return self.name == "刘备"

        elif number == 2:
            return self.name == "孙权"
        elif number == 3:
            return self.name == "曹操"

    def computer_chuquan(self):
        nub = random.randint(1, 3)
        if nub == 1:
            return nub
        elif nub == 2:
            return nub
        elif nub == 3:
            return nub

    def add_computers(self):
        self.score = self.score + 1
        return self.score

    def pin_player(self):
        self.score = self.score + 0
        return self.score

    def finaly(self, c):
        if c == 1:
            print("出了剪刀")
        elif c == 2:
            print("出了石头")
        elif c == 3:
            print("出了布")
        print("=========猜拳结果==========")


class Player:
    def __init__(self, playname):
        self.playname = playname
        self.playscore = 0

    def player_chuquan(self, number):
        self.number = number
        if number == 1:
            print("你出拳：剪刀")
        elif number == 2:
            print("你出拳：石头")
        elif number == 3:
            print("你出拳：布")

    def add_player(self):
        self.playscore = self.playscore + 1
        return self.playscore

    def pin_player(self):
        self.playscore = self.playscore + 0
        return self.playscore


class Startgame:
    def setcname(self, name):
        if name == 1:
            return '刘备'
        elif name == 2:
            return '孙权'
        elif name == 3:
            return '曹操'
        else:
            return '名字有误'


if __name__ == '__main__':
    print("--------------欢迎进入游戏世界----------------")
    print("----------------猜拳，开始-------------------")
    print("-------------------哈----------------------")
    print("出拳规则：1.剪刀 2.石头 3.布")
    # 需要取出数字对应的名称
    c = Computer("电脑的名字")  # 实例化方法
    p = Player("玩家的名字")  # 实例化方法
    s = Startgame()
    # 选择电脑的角色名
    choose_computer = int(input("请为对方选择角色(1:刘备 2:孙权 3:曹操) :"))
    s.setcname(choose_computer)
    # 创建自己的角色名
    choose_oneself = input("请输入你的姓名：")
    print("对战开始：%s Vs %s" % (s.setcname(choose_computer), choose_oneself))  # 调用方法，传入电脑的名字和自己的名字
    action = input("要开始吗？(y/n)")  # 选择游戏是是否开始

    while True:
        if action == "y":  # 开始游戏
            player = int(input("请出拳：1.剪刀 2.石头 3.布(输入对应的数字):"))
            # 玩家出拳
            p.player_chuquan(player)
            # 使用一个实例进行判断出拳
            comp_q = c.computer_chuquan()
            # 电脑出拳
            c.finaly(comp_q)
            if (player == 1 and comp_q == 3) or (player == 3 and comp_q == 2) or (
                    player == 2 and comp_q == 1):
                p.add_player()
                print("%s 恭喜你赢下这一局！" % choose_oneself)
                print("=========================")
            elif (player == comp_q):
                print("平局")
                p.pin_player(), c.pin_player()
                print("=========================")
            else:
                c.add_computers()
                print("%s赢了下了这一局，%s 你输了" % (s.setcname(choose_computer), choose_oneself))
                print("=========================")

            print("玩家的分数：%s,电脑的分数%s" % (p.playscore, c.score))
            if p.playscore == 5:
                print("游戏结束！恭喜 %s 获胜！！！" % player)
                break
            elif c.score == 5:
                print("游戏结束！恭喜 %s 获胜！！！" % s.setcname(choose_computer))
                break
            tag = input("是否继续y/n:")
            if tag.lower() == "n":
                print("退出游戏，欢迎下次再来！！！")
                break

Startgame

# a= Computer("shabi")
# a.computer_name(3)
