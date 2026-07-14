##############name##############
# DFS非再帰
######description######
# DFS非再帰
######body######

# 深さ優先探索
# 隣接リスト
# 行きかけ、帰りがけ処理


def dfs(G:list, st:int, goal=None):
    # 深さ優先探索（行きがけTrue、帰りがけFalse）
    n = len(G)
    stack = []
    seen = [False] * n
    level = [-1] * n    # 階層
    parent = [-1] * n   # 親node
    dp = [-1] * n       # dp 適宜設定
    # スタートの設定
    stack.append((False, st))
    stack.append((True, st))
    seen[st] = True
    level[st] = 0

    while stack:
        fg, cur = stack.pop()
        if fg:
        #行き掛け
            seen[cur] = True
            for nxt in G[cur]:
                if seen[nxt]: continue
                # 行きがけ処理
                parent[nxt] = cur
                level[nxt] = cur + 1
                stack.append((False, nxt))
                stack.append((True, nxt))
        ############
        else:
        #帰り掛け
            isok = True
            # dp[cur] = 1                     # ex.部分木のノード数
            for child in G[cur]:
                if parent[cur] == child: continue
                if dp[child] == 1:
                    isok = False
                # dp[cur] += dp[child]          # ex.部分木のノード数
            dp[cur] = int(isok)
            if cur == goal: return dp
        ############
    return dp

##########################################
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    # a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

dp = dfs(G, 0)
print(sum(dp))

######prefix######
# Lib_G_DFS_非再帰
##############end##############
