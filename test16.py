"""
题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

输入描述:
 输入一个整数（int类型）

输出描述:
 这个数转换成2进制后，输出1的个数

示例1
输入
5
输出
2
"""
n = int(input())
s_n = bin(n)

count = 0
for i in s_n:
    if i == '1':
        count = count + 1

print(count)
