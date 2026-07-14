####################
# EDPC F LCS
# https://atcoder.jp/contests/dp/tasks/dp_f/
####################

s = input()
t = input()

ls = len(s)
lt = len(t)

# dp[i][j]=(sをi文字目、tをj文字目までみた時の最長共通部分列の長さ)
dp = [[0]*(lt + 1) for _ in range(ls + 1)]

# dp[i][j] <- dp[i-1][j-1] + 1      if s[i]==t[j]
# dp[i][j] <- max(dp[i-1][j], dp[i][j-1])

for i in range(ls):
    for j in range(lt):
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)

i = ls
j = lt
ret = ''
while i > 0 and j >0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:   #dp[i][j] == dp[i-1][j-1]
        ret += s[i-1]
        i -= 1
        j -= 1

print(ret[::-1])
