######title######
# 三分探索
######subtitle######
# 三分探索

##############name##############
# 三分探索
######description######
# 三分探索
######body######
#######################
# ムーアの法則
# 三分探索/黄金分割探索
#######################

def f(x): return x**2

d = 0.000000001
low, high = 0, 1000

# 分割割合
alp = 1/3           #三分探索
alp = (3-5**0.5)/2  #黄金分割探索

while abs(f(low) - f(high)) > d:
    l_ = high * alp + (1-alp) * low
    h_ = high * (1-alp) + alp * low
    if f(h_) < f(l_):
        low = l_
    else:
        high = h_
print(f'{f(low):.10f}')




#######################
# 内包円
# 三分探索
# https://atcoder.jp/contests/abc151/tasks/abc151_f
# 平面上の N 個の点 (xi, yi) が与えられます。
# これら全てを内部または周上に含む円の半径の最小値を求めてください。
#######################

n = int(input())
pt = [tuple(map(int, input().split())) for i in range(n)]

def f(x, y):
    # (x, y)を与えたときに、各点との距離の最大値
    return max([((x-u)**2 + (y-v)**2)**0.5 for u, v in pt])

d = 0.0000001

def g(x):
    low, high = 0, 1000
    for i in range(80):
        l_ = (high+2*low)/3
        h_ = (high*2+low)/3
        if f(x, h_)<f(x, l_):
            low = l_
        else:
            high = h_
    return f(x, low)


low, high = 0, 1000
for i in range(80):
    l_ = (high+2*low)/3
    h_ = (high*2+low)/3
    if g(h_)<g(l_):
        low = l_
    else:
        high = h_

print(g(low))


######prefix######
# Lib_A_三分探索
##############end##############


##############name##############
# 三分探索int
######description######
# 三分探索int
######body######

def f(x): return x**2

low, high = 0, 1000
while high - low > 2:
    l_ = low + (high - low) // 3
    h_ = high - (high - low) // 3
    if f(h_) < f(l_):
        low = l_
    else:
        high = h_
ret = min(f(low), f(high))
print(ret)


######prefix######
# Lib_A_三分探索整数
##############end##############
