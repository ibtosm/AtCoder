####################
# EDPC S DigitSum
# https://atcoder.jp/contests/dp/tasks/dp_s/
####################
# 桁DP

mod = 1000000007

k = input()
d = int(input())

deg = len(k)

# dp[i][res][0] 数がk以下に未確定で和の余りがres
# dp[i][res][1] 数がk以下に確定で和の余りがres

dp = [[[0] * 2 for j in range(d)] for i in range(deg+1)]
dp[0][0][0] = 1

for i, ki in enumerate(k):
    ki = int(ki)
    for digit in range(10):
        for res in range(d):
            newres = (res+digit)%d
            # 桁が未確定のものからの遷移
            if ki == digit: # 未確定のまま
                dp[i+1][newres][0] += dp[i][res][0]
            elif ki > digit: # 確定へ
                dp[i+1][newres][1] += dp[i][res][0]
            # 桁が確定しているものからの遷移
            dp[i+1][newres][1] += dp[i][res][1]
            dp[i+1][newres][0] %= mod
            dp[i+1][newres][1] %= mod

print((sum(dp[-1][0])-1)%mod)
