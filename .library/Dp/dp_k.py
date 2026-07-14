####################
# EDPC K Stones
# https://atcoder.jp/contests/dp/tasks/dp_k/
####################
# 後退解析

n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [False] * (k + 1)
# dp[i]  i個のときの手番の人が勝てるか？

for i in range(k+1):
    for aj in a:
        nxt = i - aj
        if nxt >= 0 and not dp[nxt]: # 負けが一個でもあったら
            dp[i] = True
            break

if dp[k]:
    print('First')
else:
    print('Second')
