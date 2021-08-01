'''
@File : day01_4_字符串格式化输出.py
@Time : 2021/3/28 15:07
@Author: luoman
'''
# import lib
name = 'Lily'
age = 18
score = 99.22222
room = 701  # 假设这一栋楼有10层 1001 如果楼层小于0 左边补0变成 0701
# 按格式输出 Lily今年18岁
# print(name+'今年'+age+'岁') # 错误的输出
# 字符串的格式化输出  %字符 表示该位置有一个格式化数据
print('%s今年%d岁' % (name, age))
print('%s今天的考试成绩是%f' % (name, score))
# 保留小数位--四舍五入
print('%s今天的考试成绩是%.4f' % (name, score))
# lyli住在701  ---lyli住在0701号房间
print('%s住在%s号房间' %(name, room))
print('%s住在%04d号房间' % (name, room)) # 总共要输出4个位置宽的数据，不够的话左边补0

# 左右对齐：默认右对齐，左对齐需要加 '-' 号
print('%s住在%-6d号房间' %(name, room))
# 输出lyli考试99.99，共显示8个位置，但是左对齐
print('%s今天的考试成绩是%08.2f' % (name, score))
print('%s今天的考试成绩是%-8.2f' % (name, score))