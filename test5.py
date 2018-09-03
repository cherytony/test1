"""
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

输入描述:
输入一个正浮点数值

输出描述:
输出该数值的近似整数值

示例1
输入
5.5
输出
6
"""

import math

n = float(input())
decimal = n - int(n)
if (decimal * 10)>= 5:
    n = math.ceil(n)
else:
    n = math.floor(n)
print(n)