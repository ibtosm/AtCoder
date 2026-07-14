####################
# EDPC D Knapsack1
# https://atcoder.jp/contests/dp/tasks/dp_d/
####################
# ナップサックのコストが小さいVersion

n, w = map(int, input().split())

# dp[_x][i]: _x番目の品物でiの総和で実現できる最大価値
# dp[i]:

dp = [0] * (w + 1)

### 配るdp
for _ in range(n):
    wi, vi = map(int, input().split())
    for i in range(w+1-wi)[::-1]:
        dp[i+wi] = max(dp[i+wi], dp[i] + vi)

print(max(dp))

### 貰うdp

for _ in range(n):
    wi, vi = map(int, input().split())
    for i in range(w+1)[::-1]:
        if i - wi < 0: break
        dp[i] = max(dp[i], dp[i - wi] + vi)

print(max(dp))
