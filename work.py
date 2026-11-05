import sys

sys.setrecursionlimit(1000_000_000)


class HLD_Pathquery:
    def __init__(
        self,
        n: int,
        G,
        # G: list[list[int | tuple[int, int]]],
        root=0,
    ) -> None:

        self.n: int = n
        self.G = G
        # self.G: list[list[int | tuple[int, int]]] = G
        self.root = root

        self.parent: list[int] = [-1] * n
        self.depth: list[int] = [-1] * n
        self.size: list[int] = [0] * n
        self.head = [0] * n
        # 属するheavy pathの先頭
        self.heavy = [-1] * n
        # vのheavy child
        self.pos = [-1] * n
        # vの配列位置
        self.vertex = []
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

    def _dfs2(self, v, p) -> None:
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
            if self.pos[u] < self.pos[v]:
                u, v = v, u
            u = self.parent[self.head[u]]

        return u if self.depth[u] < self.depth[v] else v


N, Q = map(int, input().split())
G = [[] for _ in range(N)]
p = list(map(int, input().split()))
for i in range(len(p)):
    G[i + 1].append(p[i])
    G[p[i]].append(i + 1)
hld = HLD_Pathquery(N, G, 0)
for _ in range(Q):
    u, v = map(int, input().split())
    print(hld.lca(u, v))
