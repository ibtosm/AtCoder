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
# et_nodes : とおった頂点を記録
# - LCAができる
# et_edges : とおった辺を記録/パスクエリ
# - 根からある頂点へのパスのコストの総和が取れる
# - LCAと組み合わせてある頂点からある頂点までのパスのコストの総和が取れる

# https://atcoder.jp/contests/abc294/tasks/abc294_g
# https://atcoder.jp/contests/abc014/tasks/abc014_4

# https://atcoder.jp/contests/abc187/tasks/abc187_e
#

import sys
from dataclasses import dataclass
from typing import Any, TypeAlias

TourEdge: TypeAlias = tuple[int, int, int]
# (weight, edge_id, sign)

# from atcoder.lazysegtree import LazySegTree

sys.setrecursionlimit(1000_000_000)


@dataclass(slots=True)
class Edge:
    to: int
    weight: int
    index: int

    def __str__(self):
        return f"to:{self.to}, weight:{self.weight}, index:{self.index}"


class EulerTour:
    def __init__(self, n: int) -> None:
        self.n: int = n
        self.G: list[list[Edge]] = [[] for _ in range(N)]
        self.root = 0
        self.edge_count = 0

        self.depth: list[int] = [-1] * n
        # 根からの深さ

        """ preorder """
        self.pre_order: list[int] = []
        # DFSに登場する順番>len=n
        self.pre_in: list[int] = [-1] * n
        # pre_order上での頂点vの位置
        self.pre_out: list[int] = [-1] * n
        # pre_order上での頂点vを抜ける位置

        """ node euler tour """
        self.et_nodes: list[int] = []
        # 頂点版Euler Tour
        self.et_nodes_in: list[int] = [-1] * n
        # et_nodes上での最初の出現位置
        self.et_nodes_out: list[int] = [-1] * n
        # et_nodes上での最後の出現位置の直後

        """ edge euler tour """
        self.et_edges: list[TourEdge] = []
        # (weight, edge_id, sign)
        self.et_edges_in: list[int] = [-1] * n
        # 頂点へ入る辺の位置
        self.et_edges_out: list[int] = [-1] * n
        # 頂点から戻る辺の位置の直後
        self.edges_pos: list[list[int]] = []
        # edges_pos = [
        #     [0, 3],  # edge0 は et_edges[0], et_edges[3]
        #     [1, 2],  # edge1 は et_edges[1], et_edges[2]
        # ]

    def dump(self, mode: str = "all") -> None:
        sections: list[Any] = []

        if mode in ("all", "pre"):
            sections.append(
                (
                    "pre_order",
                    [
                        ("pre_order", "DFSで初回訪問した頂点順", self.pre_order),
                        ("pre_in", "pre_order上のvの位置", self.pre_in),
                        ("pre_out", "部分木区間の終端", self.pre_out),
                    ],
                )
            )

        if mode in ("all", "nodes"):
            sections.append(
                (
                    "et_nodes",
                    [
                        ("et_nodes", "頂点版EulerTour", self.et_nodes),
                        ("et_nodes_in", "最初vの出現位置", self.et_nodes_in),
                        ("et_nodes_out", "部分木を抜けた位置", self.et_nodes_out),
                    ],
                )
            )

        if mode in ("all", "edges"):
            sections.append(
                (
                    "et_edges",
                    [
                        ("et_edges", "(weight, edge_id, sign)", self.et_edges),
                        ("et_edges_in", "頂点へ入る辺の位置", self.et_edges_in),
                        ("et_edges_out", "頂点から戻る位置", self.et_edges_out),
                    ],
                )
            )

        if mode in ("all", "depth"):
            sections.append(
                (
                    "depth",
                    [
                        ("depth", "rootからの深さ", self.depth),
                    ],
                )
            )

        for title, rows in sections:
            print()
            print(f"[{title}]")
            print(f"{'name':<15} {'description':<30} value")
            print("-" * 80)

            for name, desc, value in rows:
                print(f"{name:<15} {desc:<30} {value}")

    def _dfs(self, v: int, p: int) -> None:
        #
        # depth
        #
        self.depth[v] = 0 if p == -1 else self.depth[p] + 1

        #
        # pre-order
        #
        self.pre_in[v] = len(self.pre_order)
        self.pre_order.append(v)

        #
        # Euler Tour (Vertex)
        #
        self.et_nodes_in[v] = len(self.et_nodes)
        self.et_nodes.append(v)

        #
        # child traversal
        #
        for e in self.G[v]:
            if e.to == p:
                continue

            #
            # Euler Tour (Edge) : forward
            #
            pos = len(self.et_edges)

            self.et_edges_in[e.to] = pos
            self.et_edges.append(
                (
                    e.weight,
                    e.index,
                    1,
                )
            )

            self.edges_pos[e.index].append(pos)

            #
            # dfs
            #
            self._dfs(v=e.to, p=v)

            #
            # Euler Tour (Vertex) : backtrack
            #
            self.et_nodes.append(v)

            #
            # Euler Tour (Edge) : backward
            #
            pos = len(self.et_edges)

            self.et_edges.append(
                (
                    e.weight,
                    e.index,
                    -1,
                )
            )

            self.edges_pos[e.index].append(pos)

            self.et_edges_out[e.to] = len(self.et_edges)

        #
        # subtree information
        #
        self.pre_out[v] = len(self.pre_order)

        self.et_nodes_out[v] = len(self.et_nodes)

    def add_edge(
        self,
        u: int,
        v: int,
        weight: int = 0,
    ) -> None:
        """
        無向辺を追加

        Parameters
        ----------
        u : int
            頂点 u

        v : int
            頂点 v

        weight : int
            辺重み
        """

        edge_id: Any = self.edge_count

        self.G[u].append(
            Edge(
                to=v,
                weight=weight,
                index=edge_id,
            )
        )

        self.G[v].append(
            Edge(
                to=u,
                weight=weight,
                index=edge_id,
            )
        )

        self.edges_pos.append([])
        self.edge_count += 1

    def set_euler_tour(self, root: int = 0) -> None:
        """オイラーツアーを構築"""
        self.root: int = root
        self._dfs(v=self.root, p=-1)

    def subtree_range(
        self,
        v: int,
    ) -> tuple[int, int]:
        """vの部分木のpreorderの範囲"""
        return (
            self.pre_in[v],
            self.pre_out[v],
        )

    def subtree_nodes(
        self,
        v: int,
    ) -> list[int]:
        """vの部分木のノード"""
        l, r = self.subtree_range(v)
        return self.pre_order[l:r]

    def subtree_nodes_count(self, v: int) -> int:
        """vの部分木のノード数"""
        l, r = self.subtree_range(v)
        return r - l

    def is_in_subtree(
        self,
        u: int,
        v: int,
    ) -> bool:
        """uがvの部分木に含まれているかどうか"""
        return self.pre_in[v] <= self.pre_in[u] < self.pre_out[v]


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """"""
from atcoder.segtree import SegTree

#########################################

# N, Q = map(int, input().split())
# P = list(map(int, input().split()))
# T = EulerTour(N)
# for i in range(N - 1):
#     T.add_edge(P[i] - 1, i + 1, i + 1)

# https://info.atcoder.jp/entry/algorithm_lectures/euler_tour_technique
N = 6
T = EulerTour(N)
T.add_edge(0, 3, 1)
T.add_edge(1, 3, 1)
T.add_edge(0, 2, 1)
T.add_edge(2, 4, 1)
T.add_edge(2, 5, 1)
T.set_euler_tour(root=0)
T.dump("all")


######prefix######
# Lib_GT_オイラーツアー_eulartour_subtree
##############end##############
