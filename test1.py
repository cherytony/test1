import  sys
a = {}
b = {}
n_s, m_s = sys.stdin.readline().strip().split(' ')
for i in range(0, int(n_s)):
    a_i, b_i = sys.stdin.readline().strip().split(' ')
    a[a_i] = b_i

for i in range(0, int(m_s)):
    a_i, b_i = sys.stdin.readline().strip().split(' ')
    b[a_i] = b_i

# 总的价格
def sun_no_reduced(a):
    s = 0
    for i, _ in a.items():
        s += int(i)

    return s

# 各种满减优惠方案的最优惠方案
def sun_min_reduced(s, b):
    value = s
    for i, j in b.items():

        if s >= int(i):
            m = s - int(j)
            if m < value:
                value = m

    return value

# 计算特价优惠方案
def sum_mj_reduced(a):
    sum =0
    for i , j in a.items():
        if int(j)==1:
            sum += int(i) * 0.8
        else:
            sum += int(i)
    return sum

s = sun_no_reduced(a)
sun_min_reduced = sun_min_reduced(s, b)
sum_mj_reduced = sum_mj_reduced(a)

if sun_min_reduced<sum_mj_reduced:
    print('%.2f' % sun_min_reduced)
else :
    print('%.2f' % sum_mj_reduced)