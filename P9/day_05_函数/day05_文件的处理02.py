#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day05_文件的处理02.py
@time: 2021/4/18 15:10
'''

# 创建一本空文件，取名字
wfp = open("file/今晚打老虎.txt", 'w+', encoding="utf-8")
# 写入内容
w = "今天我们想去打老虎，但是！老虎是保护动物！故！失败！！"
wl = ["因为下雨,", "所以心情不好", "故学习！!!"]
wfp.writelines(wl)  # 写入了内容以后，文件的光标到文件的最后去了
# 刷新
wfp.flush()
# 想读出书中的内容
# ws = wfp.read() 发现打印出来是空的
# 所以我们要移动光标
# 移动到文件的开头位置：第一个0表示移动的字节数，第二个0表示参照的位置，表示开头
# 参照开头移动位置
wfp.seek(3, 0)  # 一个汉字占用三个字节，表示开头移动三个字节
# wfp.seek(2,0)  # 不满足三个会报错

# tell() 告诉你光标所在的位置
print(wfp.tell())

# next() 返回下一行
ws = next(wfp)
print(ws)

# 关闭文件
wfp.close()
