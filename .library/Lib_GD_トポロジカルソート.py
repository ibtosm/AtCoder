######title######
# トポロジカルソート
######subtitle######
# 有向非巡回グラフ（DAG）の各ノードを順序付けして、どのノードもその出力辺の先のノードより前にくるように並べることである。
# 有向非巡回グラフは必ずトポロジカルソートすることができる。
# totplogical_sort(ノード数, 隣接グラフ):
# .build(sorttype): sorttype = 'appear' 出たとこ順、 = 'nodeid' ノード番号順

##############name##############
# トポロジカルソート 有向グラフ
######description######
# トポロジカルソート topologicalsort
######body######

from collections import deque

class topological_sort:
    def __init__(self, n:int, G) -> None:
        self.n = n
        self.ts = []            # トポロジカルソート
        self.parents = [-1] * n # 親 -1は根
        self.G = G              # 辺
        self.in_cnt = [0] * n   # 入力
        self.node_zero = []     # ゼロ次のノード
        for i, gi in enumerate(G):
            for j, _ in gi:
                self.in_cnt[j] += 1
        self.node_zero = [i for i in range(self.n) if self.in_cnt[i] == 0]


    def _build_sort_by_appear(self) -> None:
        q = self.node_zero[:]
        q = deque(q)
        while q:
            p = q.popleft()
            self.ts.append(p)
            for nxt, _ in self.G[p]:
                self.in_cnt[nxt] -= 1
                if self.in_cnt[nxt] == 0:
                    q.append(nxt)
                    self.parents[nxt] = p


    def _build_sort_by_nodeid(self) -> None:
        from heapq import heapify, heappop, heappush
        q = self.node_zero[:]
        heapify(q)
        while q:
            p = heappop(q)
            self.ts.append(p)
            for nxt, nxtw in self.G[p]:
                self.in_cnt[nxt] -= 1
                if self.in_cnt[nxt] == 0:
                    heappush(q, nxt)
                    self.parents[nxt] = p


    def build(self, sorttype='appear'):
        self.ts = []            # トポロジカルソート
        if sorttype == 'appear':        # 出たとこ順番
            self._build_sort_by_appear()
        elif sorttype == 'nodeid':      # ノードの順番
            self._build_sort_by_nodeid()


    @property
    def is_dag(self) -> bool:
        return len(self.ts)==self.n
        # True 閉路なしDAG
        # False 閉路あり


    @property
    def is_unique(self) -> bool:
        if not self.is_dag: return False
        for i in range(self.n-1):
            u, v = self.ts[i:i+2]
            if not v in self.G[u]: return False
        return True
        # True トポロジカルソートの経路が一意
        # False 複数あり


#########################################
# n, m = map(int, input().split())
n = int(input())
G = [[] for _ in range(n)]
m = n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    w = 0
    G[a].append(b)

ts = topological_sort(n, G)

ts.build()

print(ts.ts)
print(ts.parents)
print(ts.is_dag)
print(ts.is_unique)

######prefix######
# Lib_GD_トポロジカルソート_topologicalsort
##############end##############
