######title######
# 二部グラフ判定
######subtitle######
# 二部グラフ(bipartite graph)
# 頂点集合を2つに分割して各部分の頂点は互いに隣接しないようにできるグラフ
# ノード2色を塗って、辺の両端は異なるようにできるか

##############name##############
# 二部グラフ判定
######description######
# 隣接リストから二部グラフかどうか判定
######body######

import sys
sys.setrecursionlimit(10**9)

######################################
# 二部グラフ(bipartite graph)
# 頂点集合を2つに分割して各部分の頂点は互いに隣接しないようにできるグラフ
# ノード2色を塗って、辺の両端は異なるようにできるか
######################################
######################################
# 再帰版
######################################
# 深さ優先探索
def is_bipartite(g, v, c):
    global color
    color[v] = c    # 色を塗る
    for nv in g[v]: # 次のノードの探索
        # すでに隣接の色が確定していて同じ色となっている場合終了
        if color[nv] == c: return False
        # 未確定の倍は反転させた色を塗って探索した結果を受け取る
        if color[nv] == 0 and not is_bipartite(g, nv, -c): return False
    return True


######################################
# 非再帰版
######################################
def is_bipartite(g, st, c):
    global color
    # 深さ優先探索
    q = [(st, c)]
    while q:
        v, c = q.pop()
        color[v] = c    # 色を塗る
        for nv in g[v]: # 次のノードの探索
            # すでに隣接の色が確定していて同じ色となっている場合終了
            if color[nv] == c: return False
            # 未確定の倍は反転させた色でキューに入れる
            if color[nv] == 0:
                q.append((nv, -c))
    return True

#######################################

n, m = map(int, input().split())
G = [[] for _ in range(n)]
color = [0] * n     # 0:未確定 1:黒 -1:白

# 隣接リストの作成
for i in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

print(is_bipartite(G, 0, 1))

######prefix######
# Lib_G_二部グラフ判定_bipartite
##############end##############
