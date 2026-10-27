######title######
# 木の上の範囲クエリ
######subtitle######
# 木の上の範囲クエリ RangeQuery
# SegTree_EularTour(n ,G, node_cost): node_costなしの場合 [0] * n
# set_euler_tour(root=0): rootを親として、オイラーツアーを計算
# root_edge_dist(u:int): rootからノードuへのパス上の辺の数の合計（距離）
# root_edge_cost(u:int): rootからノードuへのパス上の辺の重み合計
# uv_edge_dist(u:int, v:int): ノードuとノードvの距離
# uv_edge_cost(u:int, v:int): ノードuとノードvのパス上の辺の重み合計
# update_edge_cost(u, v, w): エッジコストを変更
# add_edge_cost(u, v, w): エッジコストに加算
# set_query(): セグメント木の設定

# set_euler_tour(x)
##############name##############
# 木の上の範囲クエリ
######description######
# 木の上の範囲クエリ RangeQuery
######body######
#############################################
# 木の上で経路上の範囲クエリするもの
# https://atcoder.jp/contests/abc294/tasks/abc294_g

class SegmentTree:
    def __init__(self, init, f, ie):
        # initがリストなら初期化, 整数ならinit個の配列
        self._f = f
        self._ie = ie
        if type(init) == int:
            init = [ie] * init
        self._n = len(init)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self._dat = [ie] * self._size + init + [ie] * (self._size - len(init))
        for i in range(self._size-1, 0, -1): self._update(i)

    def _update(self, i):
        self._dat[i] = self._f(self._dat[i<<1], self._dat[(i<<1)+1])

    def __getitem__(self, i):
        return self._dat[i + self._size]

    def __str__(self):
        return ' '.join(map(str, (self[i] for i in range(self._n))))

    def update(self, i, x):
        # one point update  a[i] を xに更新
        i += self._size
        self._dat[i] = x
        while i:
            i >>= 1
            self._update(i)

    def add(self, i, x):
        # one point update a[i] に xを加算
        i += self._size
        self._dat[i] += x
        while i:
            i >>= 1
            self._update(i)

    def query(self, l, r):
        # 半開区間[l, r)にf(a[l], a[l+1])演算
        l += self._size
        r += self._size
        lret, rret = self._ie, self._ie
        while l < r:
            if l & 1:
                lret = self._f(lret, self._dat[l])
                l += 1
            if r & 1:
                r -= 1
                rret = self._f(self._dat[r], rret)
            l >>= 1
            r >>= 1
        return self._f(lret, rret)


class SegTree_EulerTour:
    def __init__(self, n, G, node_cost=None):
        self.n = n
        self.G = G
        self.root = None        # 根
        self.Depth = [0] * n    # 頂点iの深さ
        if node_cost:
            self.Ncost = node_cost
        else:
            self.Ncost = [0] * n       # 頂点iの値
        self.Ecost = [0] * n       # 辺iのコスト
        self.TimeIn = [0] * n   # 頂点iに到達する時間
        self.TimeOut = [0] * n  # 頂点iから抜け出す時間
        self.ETNodes = []       # ツアー順i番目の頂点番号
        self.ETDepth = []       # ツアー順i番目の深さ番号
        self.ETNodesCost = []   # ツアー順i番目の頂点のコスト
        self.ETEdgesCost = []   # ツアー順i番目の辺のコスト


    def set_euler_tour(self, root=0):
        self.root = root        # 根を設定して
        pa = [-1] * self.n
        stack = [~root, root]
        ct = -1; de = -1
        _ETedges = []
        while stack:
            v = stack.pop()
            ct += 1
            _ETedges.append(v)
            if v >= 0:
                self.TimeIn[v] = ct
                de += 1
                self.ETNodes.append(v)
                self.ETDepth.append(de)
                self.Depth[v] = de
                p = pa[v]
                for w, cost in self.G[v][::-1]:
                    if w == p: continue
                    self.Ecost[w] = cost
                    pa[w] = v
                    stack.extend([~w, w])
                self.ETNodesCost.append(self.Ncost[v])
                self.ETEdgesCost.append(self.Ecost[v])
            else:
                self.TimeOut[~v] = ct
                de -= 1
                if de < 0:
                    self.ETDepth.append(self.n)
                else:
                    self.ETDepth.append(de)
                self.ETNodes.append(pa[~v])
                self.ETNodesCost.append(-self.Ncost[~v])
                self.ETEdgesCost.append(-self.Ecost[~v])
        self.sgt_depth = SegmentTree(self.ETDepth, lambda x, y: min(x, y), float('inf'))
        self._ETedges = _ETedges
        self.set_query()
        self.parent = pa


    def lca(self, a:int, b:int):
        l = min(self.TimeIn[a], self.TimeIn[b])
        r = max(self.TimeOut[a], self.TimeOut[b])
        if l > r: l, r = r, l
        mindepth = self.sgt_depth.query(l, r)
        while r - l > 1:
            mid = (l+r) // 2
            if self.sgt_depth.query(l, mid) == mindepth:
                r = mid
            else:
                l = mid
        return self.ETNodes[l]

    def __str__(self):
        ret = ""
        ret += "[ NODE] " + " ".join(map(lambda x: str(x).rjust(4), range(self.n))) + "\n"
        ret += "[   IN] " + " ".join(map(lambda x: str(x).rjust(4), self.TimeIn)) + "\n"
        ret += "[  OUT] " + " ".join(map(lambda x: str(x).rjust(4), self.TimeOut)) + "\n"
        ret += "[DEPTH] " + " ".join(map(lambda x: str(x).rjust(4), self.Depth)) + "\n"
        ret += "[NCOST] " + " ".join(map(lambda x: str(x).rjust(4), self.Ncost)) + "\n"
        ret += "[ECOST] " + " ".join(map(lambda x: str(x).rjust(4), self.Ecost)) + "\n" * 2
        if not self.ETNodes: return ret
        ret += "[ TIME] " + " ".join(map(lambda x: str(x).rjust(4), range(len(self.ETNodes)))) + "\n"
        ret += "[ NODE] " + " ".join(map(lambda x: str(x).rjust(4), self.ETNodes)) + "\n"
        ret += "[DEPTH] " + " ".join(map(lambda x: str(x).rjust(4), self.ETDepth)) + "\n"
        ret += "[NCOST] " + " ".join(map(lambda x: str(x).rjust(4), self.ETNodesCost)) + "\n"
        ret += "[ECOST] " + " ".join(map(lambda x: str(x).rjust(4), self.ETEdgesCost)) + "\n"
        return ret

    def root_edge_dist(self, u:int): return self.Depth[u]
    def root_edge_cost(self, u:int): return self.sgt_edges.query(0, self.TimeIn[u] + 1)

    def uv_edge_dist(self, u:int, v:int):
        redist = self.root_edge_dist
        lca = self.lca(u, v)
        return redist(u) + redist(v) - 2 * redist(lca)

    def uv_edge_cost(self, u:int, v:int):
        recost = self.root_edge_cost
        lca = self.lca(u, v)
        return recost(u) + recost(v) - 2 * recost(lca)

    def update_edge_cost(self, u, v, w):
        if self.TimeIn[u] > self.TimeIn[v]: u, v = v, u
        self.sgt_edges.update(self.TimeIn[v], w)
        self.sgt_edges.update(self.TimeOut[v], -w)
        self.ETEdgesCost[self.TimeIn[v]] = w
        self.ETEdgesCost[self.TimeOut[v]] = -w

    def add_edge_cost(self, u, v, w):
        if self.TimeIn[u] > self.TimeIn[v]: u, v = v, u
        self.sgt_edges.add(self.TimeIn[v], w)
        self.sgt_edges.add(self.TimeOut[v], -w)
        self.ETEdgesCost[self.TimeIn[v]] += w
        self.ETEdgesCost[self.TimeOut[v]] -= w

    def set_query(self):
        ####################### 経路上の頂点ないしは辺の和
        self.sgt_nodes = SegmentTree(self.ETNodesCost, lambda x, y: x + y, 0)
        self.sgt_edges = SegmentTree(self.ETEdgesCost, lambda x, y: x + y, 0)


###########################################
n = int(input())
G = [[] for _ in range(n)]
edges = []
for _ in range(n-1):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    G[a].append((b, w))
    G[b].append((a, w))
    edges.append([a, b, w])

seget = SegTree_EulerTour(n, G)
seget.set_euler_tour(0)

q = int(input())
for _ in range(q):
    f, x, y = map(int, input().split())
    if f == 1:
        u, v, _ = edges[x-1]
        seget.update_edge_cost(u, v, y)
    else:
        print(seget.uv_edge_cost(x-1, y-1))


######prefix######
# Lib_GT_木上の辺の１点更新区間クエリ_RangeQuery
##############end##############
