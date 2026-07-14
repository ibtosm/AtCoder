####################
# EDPC H Grid1
# https://atcoder.jp/contests/dp/tasks/dp_h/
####################

mod = 1000000007
h, w = map(int, input().split())
grid = [input() for _ in range(h)]

dp = [[0] * w for _ in range(h)]
dp[0][0] = 1

# 貰うDP
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#': continue
        if i - 1 >= 0:
            dp[i][j] += dp[i-1][j]
        if j - 1 >= 0:
            dp[i][j] += dp[i][j-1]
        dp[i][j] %= mod

print(dp[h-1][w-1])
