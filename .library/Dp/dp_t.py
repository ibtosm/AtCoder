####################
# EDPC T - Permutation
# https://atcoder.jp/contests/dp/tasks/dp_t/
####################

mod = 1000000007

n = int(input())
s = input()

# dp[i][l]: i番目の符号を見て、N-i-1個のうち、最後に見た数字より、
# 小さい数字がl個ある


dp = [[0] * n for _ in range(n)]
dp[0] = [1] * n
sdp = [0] * n

for i in range(1, n):
    sdp[0]=dp[i-1][0]
    for l in range(1, n):
        sdp[l] = (sdp[l-1] + dp[i-1][l])%mod
    for l in range(n-i):
        if s[i-1] == '<':
            dp[i][l] = sdp[l]
        else:
            dp[i][l] = sdp[n-i] - sdp[l]
        dp[i][l]%=mod

print(dp[n-1][0])
