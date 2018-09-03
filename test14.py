"""
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符

输入描述:
将一个英文语句以单词为单位逆序排放。

输出描述:
得到逆序的句子

示例1
输入
I am a boy
输出
boy a am I
"""


def reverse(s):
    return s[::-1]


s = input().strip()
ss = reverse(s)
s_list = ss.split(" ")
print(s_list)

result = ""
for ss_list in s_list:
    ss_1 = reverse(ss_list)
    result += ss_1
    result = result + " "

print(result.strip())











