####################
# EDPC E Knapsack2
# https://atcoder.jp/contests/dp/tasks/dp_e/
####################
# ナップサックの価値が小さいVersion

n, w = map(int, input().split())

# dp[_x][i]: _x番目の品物でiの価値を実現できる最小のコスト
# dp[i]:

dp = [10**12] * 100010
dp[0] = 0

### 貰うdp
for _ in range(n):
    wi, vi = map(int, input().split())
    for i in range(100010)[::-1]:
        if i - vi < 0: break
        dp[i] = min(dp[i], dp[i - vi] + wi)

ret = 0
for i, wi in enumerate(dp):
    if wi <= w:
        ret = max(ret, i)
print(ret)

### 配るdp
for _ in range(n):
    wi, vi = map(int, input().split())
    for i in range(100010-vi)[::-1]:
        dp[i+vi] = min(dp[i+vi], dp[i] + wi)

ret = 0
for i, wi in enumerate(dp):
    if wi <= w:
        ret = max(ret, i)
print(ret)
