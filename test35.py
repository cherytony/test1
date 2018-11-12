# while True:
#     try:
#         a = int(input())
#         if a != 0:
#             print(a // 2)
#
#     except:
#         break


def fun(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fun(n - 2) + 1


def main():
    n = int(input())
    count = fun(n)
    print(count)


if __name__ == '__main__':
    main()
