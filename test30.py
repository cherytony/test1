""""
题目描述
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度超2的子串重复
说明:长度超过2的子串

输入描述:
一组或多组长度超过2的子符串。每组占一行

输出描述:
如果符合要求输出：OK，否则输出NG

示例1

输入
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000

输出
OK
NG
NG
OK
"""


def isLong(s):
    if len(s) > 8:
        return True
    else:
        return False


def isMoreClass(s):
    isNum = 0
    isBig = 0
    isSmall = 0
    isNor = 0

    for n in s:

        if (ord(n) - ord('0')) >= 0 and (ord(n) - ord('9')) <= 0:
            isNum = 1
        elif (ord(n) - ord('a')) >= 0 and (ord(n) - ord('z')) <= 0:
            isSmall = 1
        elif (ord(n) - ord('A')) >= 0 and (ord(n) - ord('Z')) <= 0:
            isBig = 1
        else:
            isNor = 1

    if isNum + isBig + isSmall + isNor >= 3:
        return True
    else:
        return False


def isSubSentence(s):
    for i in range(len(s) - 2):
        if s[i:i + 3] in s[i + 1:]:
            return False
            break

    return True


while True:
    try:
        s = input()
        if isMoreClass(s) and isSubSentence(s) and isLong(s):
            print('OK')
        else:
            print('NG')
    except:
        break

# if isLong(s):
#     print("isLong OK")
# else:
#     print("isLong NG")


# if isSubSentence(s):
#     print("isSubSentence OK")
# else:
#     print("isSubSentence NG")

# if isMoreClass(s):
#     print("isMoreClass OK")
# else:
#     print("isMoreClass NG")
