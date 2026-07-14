######title######
# 最小全域木
######subtitle######
# 最小全域木 クラスカル法 minimum_spanning_tree
# 重み付き無向グラフで、それらの全ての頂点を結び連結するような木の最小のコストを求める
# 辺の重みの小さい順にみて、連結成分が閉路にならない辺を追加していく
# つなぐ頂点が同じ連結成分にないことをUnion Find Tree でみる

##############name##############
# 最小全域木
######description######
# 最小全域木 クラスカル法 minimum_spanning_tree
# 重み付き無向グラフで、それらの全ての頂点を結び連結するような木の最小のコストを求める
# 辺の重みの小さい順にみて、連結成分が閉路にならない辺を追加していく
# つなぐ頂点が同じ連結成分にないことをUnion Find Tree でみる
######body######
from atcoder.dsu import DSU

class Kruskal:
    def __init__(self, n:int, G:list)->None:
        self.n = n
        self.all_edges = G
        self.edges = [False] * len(G)
        self.G = [[] for _ in range(n)]
        self.weight = 0
        self.nodes = set([])
        self.INF = 10**20
        self.build()

    def build(self)->None:
        uf = DSU(self.n)
        for u, v, w, i in sorted([(a, b, w, i) for i, (a, b, w) in enumerate(self.all_edges)], key=lambda x: x[2]):
            if not uf.same(u, v):
                uf.merge(u, v)
                self.weight += w
                self.nodes |= {u, v}
                self.edges[i] = True
                self.G[u].append((v, w))
                self.G[v].append((u, w))
        if sum(self.edges) != self.n - 1:   #
            self.weight = self.INF
################################

n, m = map(int, input().split())

#辺リストの作成
G = []
for i in range(m):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    G.append((a, b, w))

mst = Kruskal(n, G)
print(mst.weight)

######prefix######
# Lib_GT_最小全域木_MST
##############end##############
