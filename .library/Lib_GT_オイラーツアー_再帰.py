##############name##############
# オイラーツアー eulartour 再帰版
######description######
# オイラーツアー eulartour 再帰版
######body######
# オイラーツアー eulartour 再帰版
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
    def __init__(self, n, G):
        self.n = n
        self.edges = G
        self.root = None    # 根
        self.etnodes = []    # i番目の頂点番号
        self.etedges = []    # i番目の辺の番号
        self.etL = [-1] * n  # in time
        self.etR = [-1] * n  # out time
        self.depthbynodes = [0] * n
        self.etdepth = []       # i番目の頂点番号の深さ


    def set_euler_tour(self, root):
        self.root = root        # 根を設定して
        self._dfs(root)
        self._set_timestamp()

    def _dfs(self, cur, last=-1):
        ################## 行きがけ処理
        depth = 0
        if last != -1:
            depth = self.depthbynodes[last] + 1
        self.depthbynodes[cur] = depth
        self.etnodes.append(cur)
        self.etdepth.append(depth)

        for nxt in self.edges[cur]:
            if nxt == last: continue
            self._dfs(nxt, cur)
            ################## 帰りがけ処理
            self.etnodes.append(cur)
            self.etdepth.append(depth)


    def _set_timestamp(self):
        for ct, now in enumerate(self.etnodes):
            if self.etL[now] == -1:
                self.etL[now] = ct
            self.etR[now] = ct + 1


#########################################
def int1(x): return int(x)-1
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
#    a, b = map(int1, input().split())
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

"""
8
0 6
0 5
6 4
5 2
5 1
5 7
2 3
"""

######prefix######
# Lib_GT_オイラーツアー_再帰版_eulartour
##############end##############
