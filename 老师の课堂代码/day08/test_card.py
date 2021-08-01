'''
@File : test_card.py
@Time : 2021/5/9 08:40
@Author: luoman
'''
# import lib

from demo.card_homework import Card

f = ['A', 'K', 'Q', 'J', '10', '9', '8','7','6','5','4','3','2']
s = ['黑桃', '红桃', '梅花', '方块']

deck = [] # 存放52张牌



for s1 in s:
    for f1 in f:
        c = Card(f1, s1)
        deck.append(c)

print(len(deck))

for d in deck:
    print(d, end='\t')
    if (deck.index(d)+1) % 13 == 0:
        print()


