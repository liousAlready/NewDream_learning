'''
@File : day01_3_字符串.py
@Time : 2021/3/28 14:12
@Author: luoman
'''
# import lib
# 字符串 str
'''
# 定义字符串：需要使用引号：'  ''  三个引号 都是可以的

'''
str1 = '罗曼'
str2 = "罗曼"
str3 = """罗曼"""
print(str1)
# 三个引号  1、定义字符串  2、可以进行多行注释
# 注释：以#号开头 进行单行注释 ctrl + /  （command+/）   ''' 可以进行多行注释

str4 = 'hello,p9班的同学大家好：' \
       '大家上班辛苦啦！！'
print(str4)
str5 = '''hello,p9班的同学们大家好：
             今天长沙外面太阳很大，出去晒太阳吧！！'''
print(str5)

# 转义符：有一些特殊的符是无法直接输出的，有特殊的含义，比如说换行符
print('\n\n\n')  # \n 表示换行符
# \t 制表符
print('\t')
# 输出文件路径 \\ 表示文件的路径
print('d:\\newdream\\p9\\code')
# 就是想输出'引号 \'  \"
print('我喜欢的歌是\'种太阳\'')

# 字符串的索引--顺序
# 可以从左往右进行索引：下标是从0开始标记的
# 可以从右往左进行索引：下标是从-1开始标记的

# 字符串的切片
str6 = 'python'
# 切一个字符
print(str6[0])
print(str6[-2])
# 切出多个字符,就要有起始值和结束值：变量名[起始值:结束值]  切片：包头不包尾
print(str6[2:4])
# 如果要切到字符串的结尾
print(str6[2:])
print(str6[-4:5])
# print(str6[-4:-5]) 错误的写法

# 字符串可以进行 重复*  拼接 + : 同类型的数据类型才能拼接
print(str6 * 7)

print(str1 + str6)

# print(str6 + 10) 错误操作

# 字符串的处理函数
# 将字符串的首字母变成大写
print(str6.capitalize())
# 将字符串整个变成大写
print(str6.upper())
# 将字符串整个变成小写
print(str6.lower())
# 将字符串进行分割
str7 = 'demo.py'
print(str7.split('.'))
# 替换字符串中的字符
str8 = '2020年'
print(str8.replace('0', '1', 2))  # replace() 第一次参数是原来的字符，第二个参数是新的字符，第三个是替换的个数










