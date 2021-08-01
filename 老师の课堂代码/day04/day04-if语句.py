'''
@File : day04-if语句.py
@Time : 2021/4/11 08:21
@Author: luoman
'''
# import lib
# Python代码缩进与多行语句  {}
# if 1:
#     print('hello')
#     print('大家好')
# else:
#     print('hello....fdfdfd \
#     fsfsdfdsfsdfsd')

# 控制流语句
'''
1、顺序结构语句
2、选择结构：if..else,if ..elif...else 
   选择一个条件来执行，其它条件就不会被执行
3、循环结构：while,for
   某一个操作要重复进行多次
'''
# 1、顺序结构语句--默认执行循序
print('我是第一名执行的')
print('我是第二名执行的')
# 2、Python分支语句---选择结构
'''
if...[else....]
if...elif...[else..]

'''
'''
if 关系表达式:    #   只能是True(1),Not None 或者 Fasle(0),None
    执行语句块
[else:
    执行语句块]
'''
# 举例：今天下雨，如果没有睡醒就接着睡
if '没有睡醒':  # 在python代码中，数据处理是按照'非0即1'
    print('接着睡觉')


print('好好学习')
'''
举例：要求用户输入两个整数，比较两个数的大小，要求输出最大的
1、input('输入提示性语句')--输入的数据都是字符串
2、int()--数据强制转换
3、关系运算符 >  <
4、选择结构  
'''
a = int(input('请输入第一个整数:'))
b = int(input('请输入第二个整数:'))
if a > b:
    print('a最大为:', a)
else:
    print('b最大为:',b)

'''
if 表达式:
   执行语句块
elif 表达式:
   执行语句块
....
else:
    执行语句
'''
# 举例：对员工进行绩效考核：如果是60分以下，考核为E，如果是60--70 考核：D，  70--80  B
# 如果是80--90 A ，如果是 90--100：S
score = 82
if score < 60:
    print('你的绩效为:D')
elif score>=60 and score<70:
    print('你的绩效为:C')
elif score>=70 and score<80:
    print('你的绩效为:B')
elif score >= 80 and score < 90:
    print('你的绩效为:A')
elif 90 <= score < 100:
    print('你的绩效为:S')

# if语句的嵌套
'''

if 关系表达式:      
    if 关系表达式:    
        执行语句块
    [else:
        执行语句块]
[else:
    if 关系表达式:    
        执行语句块
    [else:
        执行语句块]
'''
# 举例：要求用户输入两个整数，比较两个数的大小，如果两个数相等，则提示：两个数相等，否则要求输出最大的
c = int(input('请输入第一个整数:'))
d = int(input('请输入第二个整数:'))
if c==d:
    print('c和d是相等的')
else:
    if c > d:
        print('c最大为:', c)
    else:
        print('d最大为:', d)







