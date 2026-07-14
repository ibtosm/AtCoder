####################
# EDPC J Sushi
# https://atcoder.jp/contests/dp/tasks/dp_j/
####################
import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
c = [0] * 4
for ai in a:
    c[ai] += 1


dp = [[[0] * (n+1) for i in range(n+1)] for j in range(n+1)]
# dp[i][j][k]: c1=i, c2=j, c3=k である時の操作回数の期待値
# dp[i][j][k] = (dp[i-1][j][k] + 1) * i/n
#             + (dp[i+1][j-1][k] + 1) * j/n
#             + (dp[i][j+1][k-1] + 1) * k/n
#             + (dp[i][j][k]   + 1)   * (n-i-j-k)/n
# = (dp[i-1][j][k]*i + dp[i+1][j-1][k]*j + dp[i][j+1][k-1]*k + n) / n
#   + dp[i][j][k] * (1 - (i+j+k)/n)


for k in range(n+1):
    for j in range(n+1-k):
        for i in range(n+1-k-j):
            if i == 0 and j == 0 and k ==0: continue
            if i: dp[i][j][k] += i * dp[i - 1][j][k]
            if j: dp[i][j][k] += j * dp[i + 1][j - 1][k]
            if k: dp[i][j][k] += k * dp[i][j + 1][k - 1]
            dp[i][j][k] += n
            dp[i][j][k] /= i + j + k
print(dp[c[1]][c[2]][c[3]])
