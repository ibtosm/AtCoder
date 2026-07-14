####################
# EDPC P Independent Set
# https://atcoder.jp/contests/dp/tasks/dp_p/
####################
# 木DP
#
import sys
sys.setrecursionlimit(10**9)
mod = 1000000007

n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges[x].append(y)
    edges[y].append(x)

dp = [[0] * 2 for _ in range(n)]

def dfs(cur, prev=-1):
    b = 1
    w = 1
    for nxt in edges[cur]:
        if nxt == prev: continue
        dfs(nxt, cur)
        b *= dp[nxt][0]
        w *= dp[nxt][0] + dp[nxt][1]
    dp[cur][1] = b%mod
    dp[cur][0] = w%mod


dfs(0)
print(sum(dp[0])%mod)
