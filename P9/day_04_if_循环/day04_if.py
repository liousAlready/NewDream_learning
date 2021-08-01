# python代码的缩进与多行语句 {}

# if 1:
#     print("hello")
#     print("大家好")
# else:
#     print("hello")

# 控制流语句
'''
1 顺序结构语句

2 选择结构语句 if...else,if..elif..else
2.1 选择一个条件来执行,其他条件就不会被执行

3 循环结构: while,for
3.1 某一个操作要重复进行执行多次
'''

# 1.顺序结构语句 -- 默认执行顺序
print("我是第一执行")
print("我是第二执行")

# python分支语句---选择结构
'''
if...[else...] else可省略
if...elif...[else...]

'''

'''

if 关系表达式: (关系表达式只能是True(1),Not None 或者False(0),None)
    执行语句块
else:
    执行语句块

'''

# 举例:今天下雨,如果没有睡醒就接着睡
if '没有睡醒':  # 在python代码中,数据处理是按照'非0即1'
    print("接着睡")

print("好好学习")

'''
举例:要求用户输入两个整数,比较两个数的大小,输出最大的
1. inpyt('输入提示性语句')--输入的数据都是字符串
2. int() --数据强制类型转换
3. 关系运算符 > < 
4. 选择结构

'''

# one = int(input("请输入第一个数: \n"))
# two = int(input("请输入第二个数: \n"))
#
# if one > two:
#     print(one, " one最大")
# else:
#     print(two, " two最大")

'''
多个判断条件
if 表达式:
    执行语句块
elif表达式:
    执行语句块
else:
    执行语句块
'''
# 举例:对员工进行绩效考核:如果是60一下,考核为D,如果是60-70 考核:D 79--80 C
# 如果是80--90 a, 如果是 90--100: s

score = 82
if score < 60:
    print("你的绩效为: D")
elif score > 60 and score <= 70:
    print("你的考核为: C")
elif score > 70 and score <= 80:
    print("你的考核为: B")
elif score > 80 and score <= 90:
    print("你的考核为: A")
elif score > 90 and score <= 100:
    print("你的考核为: S")

# if 语句嵌套
'''

if 关系表达式:
    if 关系表达式:
        执行语句块
    else:
        执行语句块
else:
    if 关系表达式:
        执行语句块
    else:
        执行语句块
'''

# 举例:要求用户输入两个整数,比较两个数的大小,如果两个数想等,则提示:两个数想等,否则要求输出最大的
c = int(input("请输入第一个数: \n"))
d = int(input("请输入第二个数: \n"))

if c == d:
    print("c跟d是相等的")
else:
    if c > d:
        print(c, " one最大")
    else:
        print(d, " two最大")

