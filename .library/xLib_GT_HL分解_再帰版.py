##############name##############
# 重軽分解 HeavyLightDecomposition_pathquery
######description######
# 重軽分解 HeavyLightDecomposition_pathquery
######body######
# 重軽分解 HeavyLightDecomposition
#

import sys

sys.setrecursionlimit(1_000_000_000)


class HeavyLightDecomposition:
    def __init__(
        self,
        n: int,
        G: list[list[int]],
        root: int = 0,
        weighted: bool = False,
    ) -> None:

        self.n: int = n
        # self.G: list[list[int]] = G
        self.root: int = root
        self.weighted: bool = weighted
        if self.weighted:
            self.WG: list[list[int]] = G
            self.G = [[] for _ in range(n)]
            for u, uedges in enumerate(G):
                for v, _w in uedges:
                    self.G[u].append(v)
        else:
            self.G: list[list[int]] = G
        self._order = 0
        self.parent: list[int] = [-1] * n
        self.depth: list[int] = [-1] * n
        self.size: list[int] = [-1] * n
        self.head: list[int] = [-1] * n
        # 属するheavy pathの先頭
        self.heavy: list[int] = [-1] * n
        # vのheavy child
        self.pos: list[int] = [-1] * n
        # vの配列位置
        self.vertex: list[int] = [-1] * n
        # 逆変換　vertex[pos[v]] = v
        self.head[self.root] = self.root
        self._dfs1(self.root, p=-1)
        self._dfs2(self.root, p=-1)
        del self._order
        del self.size
        del self.heavy
        del self.G

    def __str__(self) -> str:
        rows = [
            f"{self.__class__.__name__}(n={self.n}, root={self.root})",
            "",
            " v | id | par dep siz hed || id | vertex",
            "---+-----+--------------------++------------",
        ]

        for v in range(self.n):
            rows.append(
                f"{v:2d} | "
                f"{self.pos[v]:2d} | "
                f"{self.parent[v]:3d} "
                f"{self.depth[v]:3d} "
                f"{self.size[v]:3d} "
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
        heavy_v = -1
        for nv in self.G[v]:
            if nv == p:
                continue
            self._dfs1(nv, v)
            nvc = self.size[nv]
            self.size[v] += nvc
            if largest < nvc:
                largest = nvc
                heavy_v = nv
        self.heavy[v] = heavy_v

    def _dfs2(self, v: int, p: int) -> None:
        self.pos[v] = self._order
        self.vertex[self._order] = v
        self._order += 1
        hv = self.heavy[v]
        """hevyを先にやる"""
        if hv == -1:
            return
        self.head[hv] = self.head[v]
        self._dfs2(hv, v)
        for nv in self.G[v]:
            if nv == p or nv == hv:
                continue
            self.head[nv] = nv
            self._dfs2(nv, v)

    def la(self, v: int, d: int) -> int:
        """
        level_ancester: vの祖先で深さdのものを探す
        """
        head = self.head
        depth = self.depth
        pos = self.pos
        vertex = self.vertex
        parent = self.parent

        while True:
            h = head[v]

            if depth[h] <= d:
                # print(pos[v], d, depth[v])
                return vertex[pos[v] - (depth[v] - d)]
            v = parent[h]
        return v

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
        head = self.head
        depth = self.depth
        parent = self.parent

        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u, v = v, u
            u = parent[head[u]]

        return u if depth[u] < depth[v] else v

    def distance(self, u: int, v: int) -> int:
        depth = self.depth
        w = self.lca(u, v)
        return depth[u] + depth[v] - depth[w] * 2

    def jump(self, u: int, v: int, kth) -> int:
        """
        u -> v パス上の kth 頂点
        (u を 0 番目とする)
        """
        w = self.lca(u, v)
        depth = self.depth
        du = depth[u]
        dv = depth[v]
        dw = depth[w]
        dist = du + dv - 2 * dw
        if kth == 0:
            return u
        if dist < kth:
            return -1

        if kth < du - dw:
            return self.la(u, du - kth)
        return self.la(v, dv - (dist - kth))


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """"""

# https://info.atcoder.jp/entry/algorithm_lectures/heavy_light_decomposition
# N = 19
# EDGES = [
#     [0, 9],
#     [0, 15],
#     [10, 14],
#     [1, 10],
#     [3, 6],
#     [4, 7],
#     [4, 15],
#     [5, 15],
#     [9, 18],
#     [6, 9],
#     [2, 9],
#     [11, 12],
#     [6, 12],
#     [12, 16],
#     [8, 12],
#     [10, 18],
#     [13, 17],
#     [17, 18],
# ]

# G = [[] for _ in range(N)]
# for a, b in EDGES:
#     G[a].append(b)
#     G[b].append(a)

# T = HLD_Pathquery(n=N, G=G, root=0)

# print(T)
# n, q = map(int, input().split())
# N = int(input())
# G = [[] for _ in range(N)]
# for _ in range(N - 1):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     G[a].append(b)
#     G[b].append(a)

# lca = HeavyLightDecomposition(N, G, 0)
# Q = int(input())
# for _ in range(Q):
#     u, v = map(int, input().split())
#     u -= 1
#     v -= 1
#     # u, v, k = map(int, input().split())
#     # print(lca.jump(u, v, k))
#     print(lca.distance(u, v) + 1)

# print(T)

N, Q = map(int, input().split())
# N = int(input())
# P = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(N - 1):
    # G[P[i]].append(i + 1)
    # G[i + 1].append(P[i])
    a, b = map(int, input().split())
    # a -= 1
    # b -= 1
    G[a].append(b)
    G[b].append(a)

lca = HeavyLightDecomposition(N, G, 0)
# Q = int(input())

for _ in range(Q):
    # u, v = map(int, input().split())
    # print(lca.lca(u, v))
    u, v, k = map(int, input().split())
    print(lca.jump(u, v, k))

# print(lca)

######prefix######
# Lib_GT_重軽分解 HeavyLightDecomposition_pathquery
##############end##############
