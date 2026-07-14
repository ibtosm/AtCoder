####################
# EDPC O Matting
# https://atcoder.jp/contests/dp/tasks/dp_o/
####################
mod = 10 ** 9 + 7
n = int(input())
a = []
for i in range(n):
    a.append({i for i, xi in enumerate(list(map(int, input().split()))) if xi == 1})

# dp[_x][s] _x番目まで見て女性集合sとマッチングする場合の数
nn = 1 << n
dp = [0] * nn
dp[0] = 1


# sに関係のあるiのみ見ているので、
# 貰うdpだと遷移が少なくできる
for s in range(nn):
    i = bin(s).count('1') - 1
    for j in a[i]:
        # dp[s] <- dp[s - sの要素]
        if s >> j &1:
            dp[s] += dp[s - (1 << j)]
            dp[s] %= mod
print(dp[nn-1])

'''
これだとiとsで重複が生じる
要素数が小さいものから順に埋まればOK

for i in range(n):
    _dp = dp[:]
    for s in range(nn):
        for j in a[i]:
            if s >> j & 1: continue
            dp[s | 1 << j] += _dp[s]
            dp[s | 1 << j] %= mod
print(dp[nn-1])
'''
