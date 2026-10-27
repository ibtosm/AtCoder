##############name##############
# オイラーツアー eulartour
######description######
# オイラーツアー eulartour
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

from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree

sys.setrecursionlimit(1000_000_000)


class Edge:
    def __init__(
        self, fm: int = -1, to: int = 0, weight: int = 0, index: int = -1
    ) -> None:
        self.fm = fm
        self.to = to
        self.weight = weight
        self.index = index
        self.abs = 1

    def __str__(self):
        return f"fm:{self.fm}, to:{self.to}, weight:{self.weight}, abs:{self.abs}, index:{self.index}"


class EulerTour:
    def __init__(self, N: int) -> None:
        self.N: int = N
        self.edges = []
        self.edges_pos = []
        self.G = [[] for _ in range(N)]
        self.root: int = 0
        self.edges_count = 0
        self.build_lca_state: bool = False
        self.build_path_query: bool = False
        self.build_subtree_query = False
        self.calc_depth_state = False
        self.DEPTH = [-1] * N

        """settings"""
        self.calc_pre_order = False
        self.calc_et_nodes = False
        self.calc_et_edges = False

        """pre_order"""
        self.pre_order = [-1] * N
        self.pre_order_in = [-1] * N
        self.pre_order_out = [-1] * N
        self.pre_order_count = 0

        """eular_tour_node"""
        self.et_nodes = [-1] * (2 * N - 1)  # et上のi番目の頂点番号
        self.et_nodes_in = [-1] * N  # in time
        self.et_nodes_out = [-1] * N  # out time
        self.et_nodes_count = 0

        """eular_tour_path"""
        self.et_edges = [Edge() for _ in range(2 * N - 2)]
        self.et_edges_in = [-1] * N  # in time
        self.et_edges_out = [-1] * N  # out time
        self.et_edges_count = 0

    def __str__(self) -> str:
        ret = ""
        if self.calc_pre_order:
            ret += "--pre_order--" + "\n"
            ret += "pre_order    : " + "|".join(map(str, self.pre_order)) + "\n"
            ret += "pre_order_in : " + "|".join(map(str, self.pre_order_in)) + "\n"
            ret += "pre_order_out: " + "|".join(map(str, self.pre_order_out)) + "\n"
        if self.calc_et_nodes:
            ret += "--et_nodes--" + "\n"
            ret += "et_nodes    : " + "|".join(map(str, self.et_nodes)) + "\n"
            ret += "et_nodes_in : " + "|".join(map(str, self.et_nodes_in)) + "\n"
            ret += "et_nodes_out: " + "|".join(map(str, self.et_nodes_out)) + "\n"
        if self.calc_et_edges:
            ret += "--et_edges--" + "\n"
            ret += "et_edges    : " + "|".join(map(str, self.et_edges)) + "\n"
            ret += "et_edges_in : " + "|".join(map(str, self.et_edges_in)) + "\n"
            ret += "et_edges_out: " + "|".join(map(str, self.et_edges_out)) + "\n"
        return ret

    def _dfs(self, edge: "Edge") -> None:
        v = edge.to
        p = edge.fm
        if not self.calc_depth_state:
            self.DEPTH[v] = 0 if p == -1 else self.DEPTH[p] + 1
        if self.calc_pre_order:
            """pre_order"""
            self.pre_order_in[v] = self.pre_order_count
            self.pre_order[self.pre_order_count] = v
            self.pre_order_count += 1
        if self.calc_et_nodes:
            """et_nodes"""
            self.et_nodes_in[v] = self.et_nodes_count
            self.et_nodes[self.et_nodes_count] = v
            self.et_nodes_count += 1
        if self.calc_et_edges and p != -1:
            """et_edges"""
            self.et_edges_in[v] = self.et_edges_count
            self.et_edges[self.et_edges_count] = edge
            self.edges_pos[edge.index].append(self.et_edges_count)
            self.et_edges_count += 1

        for new_edge in self.G[v]:
            if new_edge.to == p:
                continue
            self._dfs(new_edge)
            if self.calc_et_nodes:
                """et_nodes"""
                self.et_nodes[self.et_nodes_count] = v
                self.et_nodes_count += 1

        if self.calc_pre_order:
            """pre_order"""
            self.pre_order_out[v] = self.pre_order_count
        if self.calc_et_nodes:
            """et_nodes"""
            self.et_nodes_out[v] = self.et_nodes_count
        if self.calc_et_edges and p != -1:
            """et_edges"""
            _edge = self.edges[edge.index][self.edges[edge.index][0] == edge]
            _edge.abs = -1
            self.et_edges[self.et_edges_count] = _edge
            self.edges_pos[_edge.index].append(self.et_edges_count)
            self.et_edges_count += 1
            self.et_edges_out[v] = self.et_edges_count

    def add_edge(self, u: int, v: int, weight: int = 0) -> None:
        """無向辺を設定"""
        self.edges.append(
            [Edge(u, v, weight, self.edges_count), Edge(v, u, weight, self.edges_count)]
        )
        self.edges_pos.append([])
        for _edge in self.edges[-1]:
            self.G[_edge.fm].append(_edge)
        self.edges_count += 1

    def set_euler_tour(self, root: int = 0) -> None:
        """オイラーツアーを構築"""
        self.root = root
        first = Edge()
        first.to = root
        self._dfs(first)
        self.calc_depth_state = True

    def lca(self, u: int, v: int) -> int:
        """Lowest Common Ancestor u and v"""
        if not self.build_lca_state:
            self.lca_segtree = SegTree(
                op=min,
                e=(self.N * 2, -1),
                v=[
                    (self.DEPTH[v], i)
                    for i, v in enumerate(self.et_nodes[: self.et_nodes_count])
                ],
            )
            self.build_lca_state = True
        upos = self.et_nodes_in[u]
        vpos = self.et_nodes_in[v]
        if upos > vpos:
            upos, vpos = vpos, upos
        _lca_height, lca_pos = self.lca_segtree.prod(upos, vpos + 1)
        return self.et_nodes[lca_pos]

    def _build_path_query(self) -> None:
        """path Query のセグ木を準備"""
        """Path Query SegTree"""
        if not self.build_path_query:
            self.path_segtree = SegTree(
                op=lambda x, y: x + y,
                e=0,
                v=[e.weight * e.abs for e in self.et_edges[: self.et_edges_count]],
            )
            self.build_path_query = True

    def path_dist_to_root(self, v: int):
        """Path Query SegTree"""
        self._build_path_query()
        return self.path_segtree.prod(0, self.et_edges_in[v] + 1)

    def path_query(self, u: int, v: int) -> int:
        """Path Query"""
        """Path Query SegTree"""
        self._build_path_query()

        lenu = self.path_dist_to_root(u)
        lenv = self.path_dist_to_root(v)
        len_lca = self.path_dist_to_root(self.lca(u, v))

        return lenu + lenv - len_lca * 2

    def path_update(self, i: int, weight: int) -> None:
        """Path weightの更新"""
        """Path Query SegTree"""
        self._build_path_query()
        for pos in self.edges_pos[i]:
            self.path_segtree.set(pos, weight * self.et_edges[pos].abs)

    def subtree_nodes(self, v:int)->list[int]:
        """部分木の頂点列"""
        l, r = self.subtree_range(v)
        return self.pre_order[l:r]

    def subtree_range(self, v:int)->tuple[int, int]:
        """部分木の範囲"""
        return self.pre_order_in[v], self.pre_order_out[v]

    def is_in_subtree(self, u:int, v:int)->bool:
        """uがvの部分木に入っているか"""
        return self.pre_order_in[v] <= self.pre_order_in[u] < self.pre_order_out[v]

    def _build_subtree_query(self) -> None:
        """subtree Query のセグ木を準備"""
        """subtree Query SegTree 木全体に加算"""
        if not self.build_subtree_query:
            self.subtree_segtree = LazySegTree(
                op=lambda x, y: x + y,
                e=0,
                mapping=lambda f, x: f+x,
                composition= lambda f, g:f+g,
                id_= 0,
                v=[self.node_weight[v] for v in self.pre_order],
            )
            self.build_subtree_query = True

    def add_node_weight(self, A: list[int]) -> None:
        # A は「頂点 v の重み」として渡される前提
        self.node_weight = A

    def subtree_query(self, v:int) -> int:
        """subtree の値の合算"""
        """subtree Query SegTree"""
        self._build_subtree_query()
        left, right = self.subtree_range(v)
        return  self.subtree_segtree.prod(left, right)

    def subtree_update(self, v:int, f:int) -> None:
        """subtree の値の更新"""
        """subtree Query SegTree"""
        self._build_subtree_query()
        left, right = self.subtree_range(v)
        self.subtree_segtree.apply(left, right, f)



#########################################

N, Q = map(int, input().split())
T = EulerTour(N)
P = list(map(int, input().split()))

for i in range(N - 1):
    T.add_edge(P[i] - 1, i + 1, i + 1)

T.calc_et_nodes = True
T.calc_et_edges = False
T.calc_pre_order = False

T.set_euler_tour(root=0)

for _ in range(Q):
    u, v = map(int, input().split())
    print(T.lca(u - 1, v - 1) + 1)

# LCAだけ使うとき
# T.calc_et_nodes = True

# パスクエリを使うとき
# T.calc_et_edges = True

# 部分木クエリを使うとき
# T.calc_pre_order = True
# T.add_node_weight(A)

######prefix######
# Lib_GT_オイラーツアー_eulartour
##############end##############
