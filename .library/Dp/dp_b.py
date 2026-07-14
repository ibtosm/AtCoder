####################
# EDPC B Frog2
# https://atcoder.jp/contests/dp/tasks/dp_b/
####################

n, k = map(int, input().split())
h = list(map(int, input().split()))

# dp[i] iにいる時にコストの最小値
dp = [10**10] * n
dp[0] = 0

### 配るdp
for i in range(n-1):
    for j in range(1, k+1):
        if i + j < n:
            dp[i+j] = min(dp[i] + abs(h[i+j] - h[i]), dp[i+j])
print(dp[-1])

### 貰うdp
for i in range(1, n):
    for j in range(1, k+1):
        if i-j >= 0:
            dp[i] = min(dp[i-j] + abs(h[i] - h[i-j]), dp[i])
print(dp[-1])
