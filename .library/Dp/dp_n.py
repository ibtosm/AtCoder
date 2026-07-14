####################
# EDPC N Slimes
# https://atcoder.jp/contests/dp/tasks/dp_n/
####################
# 区間DP
# 累積和を計算しておく
from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))
sum_a = list(accumulate([0] + a))
def cost(l, r):
    return sum_a[r+1] - sum_a[l]

INF = float('inf')

dp = [[INF] * n for _ in range(n)]
# dp[l][r]
# [l, r]のスライムを作り上げるための累積コスト

for i in range(n):
    dp[i][i] = 0

for d in range(1, n):
    for l in range(n):
        r = l + d
        if r == n: break
        dplr = dp[l][r]
        for k in range(l, r):
            dplr = min(dplr, dp[l][k] + dp[k+1][r])
        dp[l][r] = dplr + cost(l, r)

print(dp[0][n-1])
