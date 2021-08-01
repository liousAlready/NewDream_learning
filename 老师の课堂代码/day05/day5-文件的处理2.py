'''
@File : day5-文件的处理2.py
@Time : 2021/4/18 15:10
@Author: luoman
'''
# import lib
# 创建一本空文件，取名字
wfp = open('../file/xiaoshuo.txt', 'w+', encoding='utf-8')
# 写入的内容
wl = ['rew因为下雨,\n', '所以心情不好\n', '故学习！！\n']
wfp.writelines(wl)   # 写入了内容以后，文件的光标到文件的最后面
# 刷新
wfp.flush()
# 想读出书中的内容
# 移动光标--比如移动到文件的最前方
# seek()
# wfp.seek(0, 0) # 移动到文件的开头位置：第一个0表示移动的字节数，第二个0表示参照的位置，表示开头；参照开头移动0个字节
wfp.seek(3, 0)# 表示参照开头移动3个字节
# tell() 告诉光标所在的位置
print(wfp.tell())
#ws =wfp.read()
#print(ws)
# next()返回下一行

# while wfp is not None:
#     ws = next(wfp)
#     print(ws)

# 关闭文件
wfp.close()