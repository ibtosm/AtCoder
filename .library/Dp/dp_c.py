####################
# EDPC C Vacation
# https://atcoder.jp/contests/dp/tasks/dp_c/
####################

n = int(input())

# dp[_x][i]: _x日目にi(A=0,B=1,C=2)を選んだ時の最大幸福度
# dp[i]:
dp = [0] * 3

### 貰うdp
for _ in range(n):
    a, b, c = map(int, input().split())
    choice_a = max(dp[1], dp[2]) + a
    choice_b = max(dp[2], dp[0]) + b
    choice_c = max(dp[0], dp[1]) + c
    dp = [choice_a, choice_b, choice_c]

print(max(dp))
