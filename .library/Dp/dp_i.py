####################
# EDPC I Coins
# https://atcoder.jp/contests/dp/tasks/dp_i/
####################
import sys
def input(): return sys.stdin.readline().rstrip()


# dp[_x][i]: _x番目でi回表が出る確率
# dp[i]:

n = int(input())
p = list(map(float, input().split()))

dp = [0] * (n+1)
dp[0] = 1

for i in range(n):
    pi = p[i]
    for j in range(n)[::-1]:
        dp[j+1] *= (1 - pi)
        dp[j+1] += dp[j] * pi

print(dp[n//2+1])
