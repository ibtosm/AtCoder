##############name##############
# オイラーツアー eulartour_subtree
######description######
# オイラーツアー eulartour_subtree
######body######
# オイラーツアー eulartour
# 根付き木をDFSしたときの順番で頂点を記録する手法
# https://info.atcoder.jp/entry/algorithm_lectures/euler_tour_technique
# pre-order : 頂点に到着したら記録/部分木クエリ
# - ある頂点の部分木の頂点に対するクエリを処理（頂点の重みの総和>segtree）
# - ある頂点uがある頂点vの部分木に含まれるかを判定する（in(v)<= in(u) < out(v）)

# https://atcoder.jp/contests/abc294/tasks/abc294_g

# https://atcoder.jp/contests/abc187/tasks/abc187_e
#

import sys

sys.setrecursionlimit(1000_000_000)


class EulerTourSubtree:
    def __init__(
        self,
        n: int,
        G: list[list[int | tuple[int, int]]],
        root=0,
    ) -> None:

        self.n: int = n
        self.G: list[list[int | tuple[int, int]]] = G
        self.root = root

        self.pre_order: list[int] = []
        self.depth: list[int] = [-1] * n
        self.pre_in: list[int] = [-1] * n
        self.size: list[int] = [-1] * n
        self.parent: list[int] = [-1] * n

        self._dfs(self.root, p=-1)

    def __str__(self) -> str:
        rows: list[str] = [
            f"{self.__class__.__name__}(n={self.n}, root={self.root})",
            "",
            f"vertex    : {list(range(self.n))}",
            f"parent    : {self.parent}",
            f"depth     : {self.depth}",
            f"pre_in    : {self.pre_in}",
            f"size      : {self.size}",
            f"pre_order : {self.pre_order}",
        ]
        return "\n".join(rows)

    def _dfs(self, v: int, p: int = -1) -> None:
        # depth
        self.depth[v] = 0 if p == -1 else self.depth[p] + 1

        # pre-order
        self.pre_in[v] = len(self.pre_order)
        self.pre_order.append(v)

        # parent
        self.parent[v] = p

        # child traversal
        self.size[v] = 1
        for nv in self.G[v]:
            if not isinstance(nv, int):
                nv, *_ = nv
            if nv == p:
                continue
            # dfs
            self._dfs(v=nv, p=v)
            self.size[v] += self.size[nv]

    def subtree_l(self, v: int) -> int:
        """オイラーツア―上のサブツリーの最初"""
        return self.pre_in[v]

    def subtree_r(self, v: int) -> int:
        """オイラーツアー上の部分木区間の右端(exclusive)"""
        return self.pre_in[v] + self.size[v]

    def subtree_range(self, v: int) -> tuple[int, int]:
        return self.pre_in[v], self.pre_in[v] + self.size[v]

    def subtree_nodes(self, v: int) -> list[int]:
        """vの部分木のノード"""
        l, r = self.subtree_l(v), self.subtree_r(v)
        return self.pre_order[l:r]

    def is_in_subtree(self, u: int, v: int) -> bool:
        """uがvの部分木に含まれているかどうか"""
        return self.pre_in[v] <= self.pre_in[u] < self.pre_in[v] + self.size[v]


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """"""

# https://info.atcoder.jp/entry/algorithm_lectures/euler_tour_technique
N = 6
EDGES = [
    [0, 3],
    [1, 3],
    [0, 2],
    [2, 4],
    [2, 5],
]

G = [[] for _ in range(N)]
for a, b in EDGES:
    G[a].append(b)
    G[b].append(a)

T = EulerTourSubtree(n=N, G=G, root=0)
print(T)

######prefix######
# Lib_GT_オイラーツアー_eulartour_subtree
##############end##############
