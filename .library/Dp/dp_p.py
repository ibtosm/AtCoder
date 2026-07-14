####################
# EDPC P Independent Set
# https://atcoder.jp/contests/dp/tasks/dp_p/
####################
# 木DP
#
from collections import deque
mod = 1000000007

def dfs(g:list, st:int, gl=None):
    # 深さ優先探索（行きがけTrue、帰りがけFalse）
    n = len(g)
    q = deque()
    seen = [False] * n
    parent = [-1] * n   # 親node
    dp = [[0] * 2 for _ in range(n)]       # dp 適宜設定
    # スタートの設定
    q.append((False, st))
    q.append((True, st))
    seen[st] = True

    while q:
        fg, cur = q.pop()
        if fg:
        #行き掛け
            seen[cur] = True
            for nxt in g[cur]:
                if seen[nxt]: continue
                # 行きがけ処理
                parent[nxt] = cur
                q.append((False, nxt))
                q.append((True, nxt))
                ############
        else:
        #帰り掛け
            w, b = 1, 1
            for nxt in g[cur]:
                if parent[cur] == nxt: continue
                wc, bc = dp[nxt]
                w *= bc + wc
                b *= wc
            dp[cur] = [w, b]
    return dp


n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges[x].append(y)
    edges[y].append(x)

dp = dfs(edges, 0, None)
print(sum(dp[0])%mod)
