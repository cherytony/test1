import sys

a = sys.stdin.readline().replace('\n', '')
b = sys.stdin.readline().replace('\n', '')
c = [a[i:i + 8] for i in range(0, len(a), 8)]
d = [b[i:i + 8] for i in range(0, len(b), 8)]
z = c + d
for i in z:
    if len(i) < 8:
        x = i + (8 - len(i)) * '0'
        print(x)
    else:
        print(i)


