#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: dome.py
@time: 2021/5/9 08:46
'''

face = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
suit = ["黑桃", "红桃", "梅花", "方块"]

deck = []

c1 = Card(f[0],s[0])
print(c1 )

for s1 in s :
    for f1 in f:
        c = Card(f[s])
        deck.append(f1,s1)

for d in deck:
    print(d,end='\t')
    if (deck.index(d)+1)%13 ==0:
        print()