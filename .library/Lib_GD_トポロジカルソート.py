######title######
# トポロジカルソート
######subtitle######
# 有向非巡回グラフ（DAG）の各ノードを順序付けして、
# どのノードもその出力辺の先のノードより前にくるように並べることである。
# 有向非巡回グラフは必ずトポロジカルソートすることができる。
# totplogical_sort(ノード数, 隣接グラフ):
# .build(sorttype): sorttype = 'appear' 出たとこ順、 = 'nodeid' ノード番号順

##############name##############
# トポロジカルソート 有向グラフ
######description######
# トポロジカルソート topologicalsort
######body######


class topological_sort:
    def _nv(self, nvw) -> int:
        return nvw if type(nvw) == int else nvw[0]

    def __init__(self, N: int, G: list[list]) -> None:
        """
        self.ts: 各ノードのトポロジカル順の番号
        self.parents: 各ノードの親
        self.in_cnt: 入力の辺の数
        self.node_zero: ゼロ次のノード
        """

        self.N: int = N
        self.ts: list[int] = []
        self.parents: list[int] = [-1] * N
        self.G: list[list] = G
        self.in_cnt: list[int] = [0] * N
        for gv in G:
            for nvw in gv:
                nv: int = self._nv(nvw)
                self.in_cnt[nv] += 1
        self.node_zero: list[int] = [i for i in range(N) if self.in_cnt[i] == 0]

    def _build_sort_by_appear(self) -> None:
        from collections import deque

        self.ts = []
        que: deque[int] = deque(self.node_zero[:])
        while que:
            v: int = que.popleft()
            self.ts.append(v)
            for nvw in self.G[v]:
                nv: int = self._nv(nvw)
                self.in_cnt[nv] -= 1
                if self.in_cnt[nv] == 0:
                    que.append(nv)
                    self.parents[nv] = v

    def _build_sort_by_nodeid(self) -> None:
        from heapq import heapify, heappop, heappush

        self.ts = []
        que: list[int] = self.node_zero[:]
        heapify(que)
        while que:
            v: int = heappop(que)
            self.ts.append(v)
            for nvw in self.G[v]:
                nv: int = self._nv(nvw)
                self.in_cnt[nv] -= 1
                if self.in_cnt[nv] == 0:
                    heappush(que, nv)
                    self.parents[nv] = v

    def build(self, sorttype="appear"):
        if sorttype == "appear":  # 出たとこ順番
            self._build_sort_by_appear()
        elif sorttype == "nodeid":  # ノードの順番
            self._build_sort_by_nodeid()

    @property
    def is_dag(self) -> bool:
        return len(self.ts) == self.N
        # True 閉路なしDAG
        # False 閉路あり

    @property
    def is_unique(self) -> bool:
        if not self.is_dag:
            return False
        for i in range(self.N - 1):
            v, nv = self.ts[i : i + 2]
            if not nv in self.G[v]:
                return False
        return True
        # True トポロジカルソートの経路が一意
        # False 複数あり


#########################################
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    # a -= 1
    # b -= 1
    w = 0
    G[a].append((b, w))

ts = topological_sort(N, G)

ts.build()

print("\n".join(map(str, ts.ts)))
# print(ts.parents)
# print(ts.is_dag)
# print(ts.is_unique)

######prefix######
# Lib_GD_トポロジカルソート_topologicalsort
##############end##############
