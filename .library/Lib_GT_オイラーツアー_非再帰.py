-----------------------------------------------------------------------------------##############name##############
# オイラーツアー eulartour 非再帰版
######description######
# オイラーツアー eulartour 非再帰版
######body######
# オイラーツアー eulartour 非再帰版
# 木をDFSしたときの順番で頂点を記録する手法
# pre-order : 頂点に到着したら記録
# post-order : 頂点から離れるときに記録
# - 根付き木のある頂点からの部分木に対するクエリを処理
# - ある頂点がある頂点の部分木に含まれるかを高速に判定する
# - 上手くオイラーツアーを作るとパスのコストの総和が取れる
# n = 5
# 0
# |
# 1
# |
# 2
# |  \
# 4  3
#
# etnodes = [0,1,2,4,2,3,2,1,0]
# etdepth = [0,1,2,3,2,3,2,1,0]
# etdetL = [0,1,2,5,3]
# etdetR = [9,8,7,6,4]


class EulerTour():
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.root = None    # 根
        self.etnodes = []   # i番目の頂点番号
        self.etedges = []   # i番目の辺の番号
        self.etdepth = []   # i番目の頂点の深さ
        self.etL = [0] * n  # in
        self.etR = [0] * n  # out
        self.parent = [-1] * n  # 各頂点の親
        self.depthbynodes = [0] * n
        self.edge_id = 0
        self.edge_tuple = []

    def add_edge(self, u, v):
        self.edges[u].append((v, self.edge_id))
        self.edges[v].append((u, self.edge_id))
        self.edge_id += 1
        self.edge_tuple.append((u, v))

    def set_euler_tour(self, root):
        self.root = root        # 根を設定して
        pa = [0] * self.n
        stack = [~root, root]
        ct = -1
        de = -1
        while stack:
            v = stack.pop()
            ct += 1
            self.etedges.append(v)
            if v >= 0:
                de += 1
                self.etnodes.append(v)
                self.etdepth.append(de)
                self.depthbynodes[v] = de
                self.etL[v] = ct
                p = pa[v]
                for w, eid in self.edges[v][::-1]:
                    if w == p: continue
                    pa[w] = v
                    stack.append(~w)
                    stack.append(w)
                    self.parent[w] = v
                    self.edge_tuple[eid] = (v, w)
            else:
                de -= 1
                self.etdepth.append(de)
                self.etnodes.append(pa[~v])
                self.etR[~v] = ct

#########################################
def int1(x): return int(x)-1
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int1, input().split())
    G[a].append(b)
    G[b].append(a)

T = EulerTour(n, G)

T.set_euler_tour(0)
print(T.etnodes)
print(T.etedges)
print(T.etdepth)

print(T.etL)
print(T.etR)
print(T.depthbynodes)

######prefix######
# Lib_GT_オイラーツアー_非再帰版_eulartour
##############end##############
