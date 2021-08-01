#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day05_文件的处理.py
@time: 2021/4/18 14:30
'''

# 文件的处理
# 用的到的地方：日志文件的处理 测试数据 测试报告的生成
# 把一些数据从文件中取出来或者写进文件中

# 读数据
'''
读小说的过程：
1.有一本小说 供你读
2.打开小说
3.开始读书
4.处理内容。比如 你讲给别人挺，或者做笔记
5.关闭小说
'''
# # 打开小说
# fp = open("file/hello.txt", "r", encoding="utf-8")  # r--读 --w写 --a追加
# # 读书 读取数据
# #  fp.read() 把文件存到内存当中去并把内容取出来
# # r = fp.read()  # 读取全部内容
# # r = fp.read(10)  # 参数表示文件的个数
# # r = fp.readline()  # readline表示函数 默认读一行
# r = fp.readlines()  # readlines 表示读取全部内容，返回的是列表，以行为单位，每一行就是一个列表中的元素
# # 处理内容
# print(r)
# # 关闭书
# fp.close()

# 第二种打开方式
# with open("file/hello.txt", "r", encoding="utf-8") as fp:
#     r = fp.read()
#     print(r)
#     fp.close()


'''
写小说
1.先创建一个本空的小说，取名字
2.开始写入想写的内容
3.刷新--缓存区
4.关闭小说
'''

# 创建一本空文件，取名字
wfp = open("file/今晚打老虎.txt", 'w+', encoding="utf-8")
# 写入内容
w = "今天我们想去打老虎，但是！老虎是保护动物！故！失败！！"
wl = ["因为下雨,", "所以心情不好", "故学习！!!"]
wfp.write(w)  # write 只能传入字符串
wfp.writelines(wl)  # writelines 可以传入字符串和列表
# 刷新
wfp.flush()
# 关闭文件
wfp.close()

'''
文件的属性：
文件的名字
文件的状态
文件的编码方式
文件的访问方式
'''

print(wfp.name)  # 文件的名字
print(wfp.close())  # 查看文件是否关闭，如果关闭返回True，否则返回False
print(wfp.encoding)  # 文件的编码模式
print(wfp.mode)  # 访问方式
