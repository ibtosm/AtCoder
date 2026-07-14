######title######
# ダイクストラ法
######subtitle######
# dijkstra: 重み付き隣接リストにより単一始点最短経路のリストを作る
# O((E+V)logV)

##############name##############
# ダイクストラ法
######description######
# ダイクストラ法
# 辺の重みが小さいものから、決めていく

######body######
# ダイクストラ法
# 重み付きグラフ関係により最短経路のリストを作る
# 有向グラフで優先度付きキューで探索
# https://atcoder.jp/contests/abc035/tasks/abc035_d
# O((E+V)logV)
from heapq import heapify, heappop, heappush
class dijkstra:
    def __init__(self, n, G):
        self.INF = 10**9
        self.n = n                  # ノード数
        self.G = G                  # 有向グラフ
        self.start = None           # 始点
        self.G_used = [None] * n    # 最短経路木の親
        self.dist = [self.INF] * n  # 始点からの距離
        # self.count = [0] * n        # 始点からの最短到達パス数

    def build(self, start):
        self.start = start
        self.G_used = [None] * self.n
        self.dist = [self.INF] * self.n
        # self.count = [0] * self.n
        next_q = []
        if type(start) is int:
            start = [start]
        for st in start:
            self.dist[st] = 0
            # self.count[st] = 1
            next_q.append((0, st))
        heapify(next_q)
        while next_q:
            d, x = heappop(next_q)
            if self.dist[x] < d: continue
            for nx, d_nx_x in self.G[x]:
                # 変則的な距離の場合はここを調整 ##
                nd = self.dist[x] + d_nx_x
                ############################
                if self.dist[nx] < nd: continue
                if self.dist[nx] == nd:
                    # self.count[nx] += self.count[x]
                    continue
                self.dist[nx] = nd
                self.G_used[nx] = x
                # self.count[nx] = self.count[x]
                heappush(next_q, (nd, nx))


    def get_dist(self, goal):
        # 各ノードへの最短距離
        return self.dist[goal]


    def get_count(self, goal):
        # 各ノードへの最短距離のパス数
        return self.count[goal]


    def get_path(self, goal):
        # 各ノードへの最短パス
        path = []
        node = goal
        while node != None:
            path.append(node)
            node = self.G_used[node]
        return path[::-1]

##########################################

n, m, t = map(int, input().split())
G = [[] for _ in range(n)]
G_R = [[] for _ in range(n)]    #行きと帰りを分けた（有向グラフ）場合
#リストの作成
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    G[a].append((b,c))
    G[b].append((a,c))
    G_R[b].append((a,c))        #行きと帰りを分けた（有向グラフ）場合

dij = dijkstra(n, G)  #クラスのインスタンス化
dijR = dijkstra(n, G_R)
dij.build(0)
dijR.build(0)

print(dij.get_dist(n-1))



####################################
"G = [[INF] * n for _ in range(n)] 版"

from heapq import heappop, heappush
def dijkstra(n, G, start):
    INF = 10 ** 20
    dist = [INF] * n
    dist[start] = 0
    que = [(0, start)]
    while que:
        d, x = heappop(que)
        if d != dist[x]: continue
        for nx in range(n):
            if x == nx: continue
            nd = d + G[x][nx]
            if nd >= dist[nx]: continue
            dist[nx] = nd
            heappush(que, (nd, nx))
    return dist


######prefix######
# Lib_SP_最短経路探索_dijkstra
##############end##############
