####################
# EDPC U Grouping
# https://atcoder.jp/contests/dp/tasks/dp_u/
####################

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = 1 << n
# dp[s] sの集合のうさぎを分類した時の最大値

dp = [0] * m
cost = [0] * m
for s in range(m):
    for i in range(n):
        for j in range(i):
            if (s >> i & 1) and (s >> j & 1):
                cost[s] += a[i][j]

for s in range(m):
    u = s
    # 部分集合を分割して探索
    while u:
        dp[s] = max(dp[s], dp[s-u] + cost[u])

        u = (u - 1) & s

print(dp[m-1])
