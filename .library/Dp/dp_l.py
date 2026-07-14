####################
# EDPC L Deque
# https://atcoder.jp/contests/dp/tasks/dp_l/
####################
# 区間DP

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * 3030 for _ in range(3030)]
# dp[d][l]
# 残りd個で[l, l+d-1]の範囲があるときのX-Y

for d in range(1, n+1):
    for l in range(n):
        r = l + d - 1
        if r == n: break
        if (n-d)%2==0:
            dp[d][l] = dp[d-1][l] + a[r]
            if d > 1:
                dp[d][l] = max(dp[d][l], dp[d-1][l+1] + a[l])
        else:
            dp[d][l] = dp[d-1][l] - a[r]
            if d > 1:
                dp[d][l] = min(dp[d][l], dp[d-1][l+1] - a[l])
print(dp[n][0])
