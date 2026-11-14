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
    ) -> None:

        self.n: int = n
        self.root = root
        parent: list[int] = [-1] * n
        depth = [0] * n
        size = [1] * n

        """""" """ dfs1 """ """"""
        """
            親と深さと部分木サイズを記録する
            orderは、Gの順番
        """
        _heavy = [-1] * n
        _order = [root]
        for v in _order:
            for nv in G[v]:
                if nv == parent[v]:
                    continue
                parent[nv] = v
                depth[nv] = depth[v] + 1
                _order.append(nv)

        for v in reversed(_order):
            mx = 0
            for nv in G[v]:
                if nv == parent[v]:
                    continue

                size[v] += size[nv]

                if size[nv] > mx:
                    mx = size[nv]
                    _heavy[v] = nv

        """""" """ dfs2 """ """"""
        """
            親と深さと部分木サイズを記録する
            orderは、Gの順番
        """
        head: list[int] = [-1] * n
        pos: list[int] = [-1] * n
        vertex: list[int] = [-1] * n

        head[root] = root

        k = 0
        _stack: list[tuple[int, int]] = [(root, root)]

        while _stack:
            v, h = _stack.pop()
            head[v] = h
            pos[v] = k
            vertex[k] = v
            k += 1

            # light child
            for nv in G[v]:
                if nv == parent[v] or nv == _heavy[v]:
                    continue
                _stack.append((nv, nv))

            # heavy child
            if _heavy[v] != -1:
                _stack.append((_heavy[v], h))

        self.parent = parent
        self.depth = depth
        self.size = size
        self.head = head
        # 属するheavy pathの先頭
        self.pos = pos
        # vの配列位置
        self.vertex = vertex
        # 逆変換　vertex[pos[v]] = v

    def __str__(self) -> str:
        rows = [
            f"{self.__class__.__name__}(n={self.n}, root={self.root})",
            "",
            " v | id | par dep siz hed || id | vertex",
            "---+----+-----------------++----+-------",
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
            # print(v, d, h)

            if depth[h] <= d:
                return vertex[pos[v] - (depth[v] - d)]
            v = parent[h]

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

        up = du - dw
        down = dv - dw
        dist = up + down

        if dist < kth:
            return -1

        if kth <= du - dw:
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

print(lca)

######prefix######
# Lib_GT_重軽分解 HeavyLightDecomposition_pathquery
##############end##############
