'''
@File : day05-文件的处理.py
@Time : 2021/4/18 14:30
@Author: luoman
'''
# import lib

# 比如日志的处理  测试数据  测试报告的生成
# 把一些数据从文件中取出来或者写进文件中
# 读数据
'''
读小说的过程
1、有一本小说供你读  --hello.txt
2、打开小说
3、开始读书
4、处理内容，比如 你讲给别人听，或者做笔记，。。。
5、关闭小说
'''
'''
# 打开hello.txt
fp = open('../file/hello.txt', 'r', encoding='utf-8')  # r--读 w--写  a--追加
# 读书
# r = fp.read(10)  # 读取全部的内容,返回的是字符串， 参数表示字符的个数
# r = fp.readline()   # 读一行  参数表示字符的个数，不表示行数
r = fp.readlines()  # 读取全部的内容，返回的是列表，以行为单位，每一行就是一个列表中的元素
print(r[1])
# 处理内容
print(r)
# 关闭书
fp.close()
'''
'''
with open('../file/hello.txt', 'r', encoding='utf-8') as fp:
    r = fp.read()
    print(r)
    fp.close()

'''
'''
写小说
1、先创建一本空小说，取名字
2、写入想写的内容
3、刷新
4、关闭小说
'''
# 创建一本空文件，取名字
wfp = open('../file/xiaoshuo.txt', 'w+', encoding='utf-8')
# 写入的内容
w = '今天我们想一起去放风筝，但是下雨！！故失败！！'
wl = ['因为下雨,\n', '所以心情不好\n', '故学习！！\n']
wfp.write(w)  # 只能传入字符串
wfp.writelines(wl)   # 可以传入字符串和列表
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
print(wfp.name)
print(wfp.closed)  # 如果已经关闭，返回True ,否则返回false
print(wfp.encoding)
print(wfp.mode)

