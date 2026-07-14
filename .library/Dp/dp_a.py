####################
# EDPC A Frog1
# https://atcoder.jp/contests/dp/tasks/dp_a/
####################

n = int(input())
h = list(map(int, input().split()))

# dp[i] iにいる時にコストの最小値
dp = [10**10] * n
dp[0] = 0

### 配るdp
for i in range(n-1):
    if i+2 < n:
        dp[i+2] = min(dp[i] + abs(h[i+2] - h[i]), dp[i+2])
    if i+1 < n:
        dp[i+1] = min(dp[i] + abs(h[i+1] - h[i]), dp[i+1])
print(dp[-1])


### 貰うdp
for i in range(1, n):
    if i-2 >= 0:
        dp[i] = min(dp[i-2] + abs(h[i] - h[i-2]), dp[i])
    if i-1 >= 0:
        dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i])
print(dp[-1])
