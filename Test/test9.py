'''
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

输入描述:
输入一个int型整数

输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

示例1
输入
9876673

输出
37689
'''

s=input()
list=[]
for i in s[::-1]:
    if i not in list:
        list.append(i)
str=''
for i in list:
    str+=i
print(str)


