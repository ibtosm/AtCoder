######title######
# 強連結成分分解

######subtitle######
# 強連結成分分解(SCC): グラフに対するSCCを行う

##############name##############
# 強連結成分分解
######description######
# 強連結成分分解(SCC): グラフに対するSCCを行う
######body######
from atcoder.scc import SCCGraph as _SCCG

class SCCGraph(_SCCG):
    def __init__(self, n):
        super().__init__(n)
        self.n = None       # 連結成分の個数
        self.ids = None     # nodeが、どのグループに属するか
        self.groups = None  # グループに属するもとのnode
        self.G = None       # 縮約後の隣接リスト

    def scc(self):
        n, ids = self._internal.scc_ids()
        groups = [[] for _ in range(n)]
        for i in range(self._internal._n):
            groups[ids[i]].append(i)
        self.n = n
        self.ids = ids
        self.groups = groups
        return n, ids, groups

    def dag(self):
        self.G = [set() for _ in range(self.n)]
        for fm, to in self._internal._edges:
            fm = self.ids[fm]; to = self.ids[to]
            if fm != to:
                self.G[fm].add(to)
        return self.G

n, m = map(int, input().split())
A = list(map(int, input().split()))
scc = SCCGraph(n)

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    if A[a] <= A[b]:
        scc.add_edge(a, b)
    if A[a] >= A[b]:
        scc.add_edge(b, a)

scc.scc()
scc.dag()

# 強連結成分分解(SCC): グラフに対するSCCを行う
# https://hkawabata.github.io/technical-note/note/Algorithm/graph/scc.html
# 有向グラフで、互いに行き来できる連結成分を分類する
# 元の有向グラフが DAG でなくとも、そのグラフの SCC は DAG を形成する
# 作り方
# 適当に選んだ頂点から深さ優先（帰りがけ探索）し、1から番号を増やしながらラベリング：
# エッジをすべて逆向きにしたグラフを用意：
# 頂点のうち、ラベル番号が最大のものを選んでグラフ探索 → 通った頂点はすべて1つの SCC に属する：
# 未探索の頂点のうち、ラベル番号が最大のものを選んでグラフ探索 → 通った頂点はすべて1つの SCC に属する：

# https://atcoder.jp/contests/practice2/tasks/practice2_g

######prefix######
# Lib_GD_強連結成分分解_SCC
##############end##############
