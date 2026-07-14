####################
# EDPC X - Tower
# https://atcoder.jp/contests/dp/tasks/dp_x/
####################
# 最適な順番があり、その順番を固定できる場合


# すでに積み上げたものの重さの総和 Aとすると
# (w1, s1, v1) と(w2, s2, v2)のどちらが優先されるか
# A<=s1, A<=s2
# 置いた後
# (1を置いた)   (2を置いた)
#   A+w1        A+w2
#   A+w1<=s2    A+w2<=s1だったらどちらも次のステップで置くことができる。
#   A+w1>s2     A+w2<=s1だったら？
#   s2<A+w1     A+w2<=s1
#   s2+A+w2<A+w1+s1
#   s2+w2  <w1+s1
# si+wiが小さいほうから置くほうがよい
#####
# iを選べば、置いたものの総和A<=si+wiが保証されている->次の奴は置くことができる
#####


import sys
from operator import itemgetter
def input(): return sys.stdin.readline().rstrip()

n = int(input())
blocks = []
for _ in range(n):
    w, s, v = map(int, input().split())
    blocks.append((w, s, v, s+w))
blocks.sort(key=itemgetter(3))

# dp[i][j]:  iまで見て、総合計の重さがjの最大価値
dp = [[-1] * 20010 for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    w, s, v, _ = blocks[i]
    for j in range(20010)[::-1]:
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if s >= j - w >= 0 and dp[i][j-w] != -1:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w] + v)
print(max(dp[n]))
