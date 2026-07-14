######title######
# ベルマンフォード法
######subtitle######
# bellman_ford: 重み付き隣接リストにより単一始点最短経路のリストを作る
# 負閉路OK  O((E+V)logV)

##############name##############
# ベルマンフォード法
######description######
# ベルマンフォード法・負閉路OK
# O(NM)
######body######
# ベルマンフォード法
# 重み付きグラフ関係により最短経路のリストを作る
# 辺を繰り返しみて、最小化していく
# |V|回更新するとで収束する/しなければ、負の閉路がある

# https://atcoder.jp/contests/abc061/tasks/abc061_d

def bellman_ford(G, st=0):
    """
    n: グラフの頂点数
    st: 始点
    G[v] = [(w, cost), ...]: 頂点vからコストcostで到達できる頂点w
    returns
    dist or -1 if 閉路あり
    """

    INF = 1e18
    dist = [INF] * n
    dist[st] = 0
    prev = [-1] * n
    for _ in range(n):
        update = False
        for v, e in enumerate(G):
            for t, cost in e:
                if dist[v] == INF: continue
                if dist[v] + cost >= dist[t]: continue
                dist[t] = dist[v] + cost
                prev[t] = v
                update = True
                upi = t
        if not update: return dist  # prev
    # 負閉路検出処理
    dist[upi] = -INF
    for _ in range(n):
        update = False
        for v, e in enumerate(G):
            for t, cost in e:
                if dist[v] == INF: continue
                if dist[v] + cost >= dist[t]: continue
                dist[t] = dist[v] + cost
                update = True
                upi = t
        if not update: return dist
    return -1

######################################

n, m = map(int, input().split())
G = [[] for _ in range(n)]
# 隣接リストの作成
for _ in range(m):
    _a, _b, _c = map(int, input().split())
    _a -= 1; _b -= 1
    G[_a].append((_b, -_c))

st = 0
ret = bellman_ford(G, st)
if ret == -1:
    print('inf')
else:
    print(-ret[-1])

######prefix######
# Lib_SP_最短経路探索_bellmanford
##############end##############
