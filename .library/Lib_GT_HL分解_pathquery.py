##############name##############
# 重軽分解 HeavyLightDecomposition_pathquery
######description######
# 重軽分解 HeavyLightDecomposition_pathquery
######body######
# 重軽分解 HeavyLightDecomposition
#

import sys

sys.setrecursionlimit(1000_000_000)


class HLD_Pathquery:
    def __init__(
        self,
        n: int,
        G: list[list[int | tuple[int, int]]],
        root=0,
    ) -> None:

        self.n: int = n
        self.G: list[list[int | tuple[int, int]]] = G
        self.root: int = root

        self.parent: list[int] = [-1] * n
        self.depth: list[int] = [-1] * n
        self.size: list[int] = [-1] * n
        self.head: list[int] = [-1] * n
        # 属するheavy pathの先頭
        self.heavy: list[int] = [-1] * n
        # vのheavy child
        self.pos: list[int] = [-1] * n
        # vの配列位置
        self.vertex: list[int] = []
        # 逆変換　vertex[pos[v]] = v
        self._dfs1(self.root, p=-1)
        self._dfs2(self.root, p=-1)

    def __str__(self) -> str:
        rows = [
            f"{self.__class__.__name__}(n={self.n}, root={self.root})",
            "",
            " v | id | par dep siz hvy hed || id | vertex",
            "---+-----+--------------------++------------",
        ]

        for v in range(self.n):
            rows.append(
                f"{v:2d} | "
                f"{self.pos[v]:2d} | "
                f"{self.parent[v]:3d} "
                f"{self.depth[v]:3d} "
                f"{self.size[v]:3d} "
                f"{self.heavy[v]:3d} "
                f"{self.head[v]:3d} || "
                f"{v:2d} | "
                f"{self.vertex[v]:3d}"
            )

        return "\n".join(rows)

    def _dfs1(self, v: int, p: int) -> None:
        self.size[v] = 1
        self.parent[v] = p
        self.depth[v] = 0 if p == -1 else self.depth[p] + 1
        largest = 0
        for i in range(len(self.G[v])):
            nv = self.G[v][i]
            if not isinstance(nv, int):
                nv, _ = nv
            if nv == p:
                continue
            self._dfs1(nv, v)
            nvc = self.size[nv]
            self.size[v] += nvc
            if largest < nvc:
                largest = nvc
                self.G[v][0], self.G[v][i] = self.G[v][i], self.G[v][0]
                self.heavy[v] = nv

    def _dfs2(self, v:int, p:int) -> None:
        self.pos[v] = len(self.vertex)
        self.vertex.append(v)
        for i in range(len(self.G[v])):
            nv = self.G[v][i]
            if not isinstance(nv, int):
                nv, _ = nv
            if nv == p:
                continue
            is_heavy = i == 0
            self.head[nv] = self.head[v] if is_heavy else nv
            self._dfs2(nv, v)

    def lca(self, u: int, v: int) -> int:
        """
        最小共通祖先 (Lowest Common Ancestor)
        重軽分解を用いて LCA を O(log N) で求める。

        head[u] と head[v] が異なる間は、
        より深い heavy path の先頭を親へ飛ばす。

        同じ heavy path に入ったら、
        深さの浅い方が LCA。

        Parameters
        ----------
        u, v : int
            ノード番号

        Returns
        -------
        int
            u と v の最小共通祖先
        """
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] < self.depth[self.head[v]]:
                u, v = v, u
            u = self.parent[self.head[u]]

        return u if self.depth[u] < self.depth[v] else v


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """"""

# https://info.atcoder.jp/entry/algorithm_lectures/heavy_light_decomposition
N = 19
EDGES = [
    [0, 9],
    [0, 15],
    [10, 14],
    [1, 10],
    [3, 6],
    [4, 7],
    [4, 15],
    [5, 15],
    [9, 18],
    [6, 9],
    [2, 9],
    [11, 12],
    [6, 12],
    [12, 16],
    [8, 12],
    [10, 18],
    [13, 17],
    [17, 18],
]

G = [[] for _ in range(N)]
for a, b in EDGES:
    G[a].append(b)
    G[b].append(a)

T = HLD_Pathquery(n=N, G=G, root=0)

print(T)

######prefix######
# Lib_GT_重軽分解 HeavyLightDecomposition_pathquery
##############end##############
