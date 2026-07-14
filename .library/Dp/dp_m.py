####################
# EDPC M Candies
# https://atcoder.jp/contests/dp/tasks/dp_m/
####################
# 三重ループにおいて、累積和を使って計算量を抑える

mod = 1000000007
from itertools import accumulate
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# 愚直
dp = [0] * (k+1)
# dp[_i]][j]: i番目まで見て、合計jとなる場合の数
dp[0] = 1
dp_sum = list(accumulate(dp))

for i, ai in enumerate(a):
    for j in range(k+1):
        if j-ai-1>=0:
            dp[j] = dp_sum[j] - dp_sum[j-ai-1]
        else:
            dp[j] = dp_sum[j]
        dp[j] %= mod
    dp_sum = list(accumulate(dp))

print(dp[-1])

'''
# 愚直
dp = [[0] * (k+1) for _ in range(n+1)]
# dp[i][j]: i番目まで見て、合計jとなる場合の数
dp[0][0] = 1
rdp = list(accumulate(dp[0]))

for i, ai in enumerate(a):
    for j in range(k+1):
        if j-ai-1>=0:
            dp[i+1][j] += rdp[j] - rdp[j-ai-1]
        else:
            dp[i+1][j] += rdp[j]
        dp[i+1][j] %= mod
    rdp = list(accumulate(dp[i+1]))

print(dp[-1][-1])
'''
