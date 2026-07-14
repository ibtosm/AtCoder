##############name##############
# Lib_G_グラフ橋関節_lowlink
######description######
# グラフの橋・関節をO(n)で検出
######body######
#関節 https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
#橋 https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_B

class LowLink():
    def __init__(self, G):
        self.n = len(G)
        self.ord = [None]*self.n    # DFS 行きがけ順
        self.low = [None]*self.n    # lowlink
        self.son = [[] for _ in range(self.n)]  # son[i] := 頂点iの子を格納したlist
        self.back_edge = [[] for _ in range(self.n)] # back_edge[i] := 頂点iから出る後退辺の終点を格納したlist
        self.tps = []                           # 頂点のトポロジカルソート
        self.bridges = []

    def build(self, root=0):
        # DFSでord, son, tpsを求め、lowを初期化
        time = 0 # DFSでの行きがけ順
        stack = [(None, root)] # 直前にいた頂点, 今いる頂点
        while stack:
            pre, now = stack.pop()
            if self.ord[now] is not None: # 後退辺を通ってきた場合
                if self.ord[pre] < self.ord[now]: continue # 後退辺を根側から進んでいた場合は無視
                self.low[pre] = min(self.low[pre], self.ord[now]) # low[pre]をord[now]でchmin
                self.back_edge[pre].append(now)
                continue
            if pre is not None: self.son[pre].append(now)   # 親子関係を記録
            self.tps.append(now)
            self.ord[now] = time
            self.low[now] = self.ord[now] # low[now]をord[now]で初期化
            time += 1
            for next in G[now]:
                if next == pre: continue
                stack.append((now, next))
        for u in reversed(self.tps):# トポソ逆順にlowを求める
            for v in self.son[u]:
                self.low[u] = min(self.low[u], self.low[v])
            for v in self.son[u]:
                if self.low[v] > self.ord[u]:
                    self.bridges.append((min(u, v), max(u, v)))

    def two_edge_connected_component(self):
        # 二重辺連結成分分解
        tecc = []                   # tecc[i] := 連結成分iの頂点グループ
        tecc_idx = [None]*self.n    # tecc_idx[i] := 頂点iが属する連結成分ID
        tecc_tree = []              # 連結成分を頂点、橋を辺としたグラフ(木)の隣接リスト

        sub_roots = [(None, 0)]     # 橋を見つけるごとに、その先は部分木として別にDFSしなおす。
        idx = 0     # 今いる頂点の連結成分の番号
        while sub_roots:
            stack = [sub_roots.pop()] # 部分木の根からDFS
            tecc.append([]) # 今いる頂点の連結成分を格納するlistを追加
            tecc_tree.append([]) # 今いる頂点の連結成分の隣接先を格納するlistを追加
            while stack:
                pre, now = stack.pop()
                tecc[idx].append(now)   # 今いる頂点を連結成分idxに追加
                tecc_idx[now] = idx     # 今いる頂点の連結成分の番号idxを記録
                if pre is not None and idx != tecc_idx[pre]: # 直前に橋を通ってきていたら
                    tecc_tree[idx].append(tecc_idx[pre]) # その橋で繋がれた2つの連結成分を辺で結ぶ
                    tecc_tree[tecc_idx[pre]].append(idx)
                for next in self.son[now]:
                    if self.low[next] > self.ord[now]: # 橋なら
                        sub_roots.append((now, next)) # その先は別の連結成分
                    else:
                        stack.append((now, next)) # その先は同じ連結成分なのでDFSを続ける
            idx += 1
        return tecc, tecc_idx, tecc_tree

    def biconnected_component(self):
        # 二重頂点連結成分分解
        bce = [] # bce[i] := 連結成分iに属する辺を格納したlist
        bcv = [] # bcv[i] := 連結成分iに属する頂点を格納したlist
        is_ap = [False]*self.n # is_ap[i] := 頂点iは関節点であるか(True/False)
        sub_roots = [(None, 0)] #「ある子に対する関節点」を見つけるごとに、その子以降は部分木として別にDFSしなおす。
        idx = 0 # 今いる頂点の連結成分の番号
        while sub_roots:
            stack = [sub_roots.pop()] # 部分木の根からDFS
            bce.append([]) # 今いる頂点の連結成分に含まれる辺を格納するlistを追加
            bcv.append([]) # 今いる頂点の連結成分に含まれる頂点を格納するlistを追加
            if stack[0][0] is not None: # 直前に通った頂点(関節点)が存在するなら
                bcv[idx].append(stack[0][0]) # それを連結成分idxに追加
            while stack:
                pre, now = stack.pop()
                if pre is not None: # 直前に通った辺が存在するなら
                    bce[idx].append((pre, now)) # 通ってきた辺を連結成分idxに追加
                bcv[idx].append(now) # 今いる頂点を連結成分idxに追加
                if now == 0: # 今いる頂点nowが根で
                    if len(self.son[now]) >= 2: # 関節点であるなら
                        for next in self.son[now]:
                            is_ap[now] = True # 関節点であことを記録
                            sub_roots.append((now, next)) # その先は別の連結成分
                        bce.pop() # 「根の関節点のみ」の連結成分は存在しないが追加してしまっているので、例外的に削除する
                        bcv.pop()
                        idx -= 1
                    else: # 関節点でないなら
                        for next in self.son[now]:
                            stack.append((now, next)) # その先は同じ連結成分なのでDFSを続ける
                else: # 根でなく
                    for next in self.son[now]:
                        if self.low[next] >= self.ord[now]: # 子nextに対して関節点なら
                            is_ap[now] = True # 関節点であることを記録
                            sub_roots.append((now, next)) # その先は別の連結成分
                        else: # 関節点でないなら
                            stack.append((now, next)) # その先は同じ連結成分なのでDFSを続ける
                if now == 0 and len(self.son[now]) <= 1:
                    for back in self.back_edge[now]: # 今いる頂点から出る後退辺は同じ連結成分なので
                        bce[idx].append((now, back)) # 連結成分idxに追加
            idx += 1
        return bce, bcv, is_ap

    # block-cut treeを構築
    def block_cut_tree(self):
        bce, bcv, is_ap = self.biconnected_component() # 二重頂点連結成分分解
        num_ap = sum(is_ap) # 関節点の個数
        bc = [[] for _ in range(num_ap+len(bcv))]
        # bc[i] := block-cut tree上の頂点iに対応する頂点を格納したlist
        # [0:num_ap)は関節点に対応する頂点で、その関節点のみがlistに含まれる
        # [num_ap:len(bc))は連結成分に対応する頂点で、その連結成分から関節点を除いたものがlistに含まれる
        # block-cut tree上の頂点iが関節点に対応している ⇔ i < num_ap
        bc_idx = [None]*self.n
        # bc_idx[i] := (元グラフの)頂点iが属するblock-cut tree上の頂点の番号(bc, bc_treeのindexに対応)
        # 関節点でない頂点iについて、対応するbce, bcvのindexが知りたい場合、bc_idx[i]-num_apで取得可能。
        bc_tree = [[] for _ in range(num_ap+len(bcv))] # bc_tree[i] := block-cut tree上の頂点iの隣接頂点を格納したlist
        idx = 0 # 今見ているblock-cut tree上の頂点番号
        for v in range(self.n): # (元グラフの)各頂点vについて
            if is_ap[v]: # 関節点なら
                bc[idx].append(v) # block-cut tree上の頂点idxにvを対応させる
                bc_idx[v] = idx
                idx += 1
        for bcv_i in bcv: # 各連結成分の
            for v in bcv_i: # 各頂点vについて
                if is_ap[v]: # 関節点なら
                    bc_tree[idx].append(bc_idx[v]) # block-cut tree上の頂点idxと関節点vに対応した頂点を辺で結ぶ
                    bc_tree[bc_idx[v]].append(idx)
                else: # そうでないなら
                    bc[idx].append(v) # block-cut tree上の頂点idxに対応した頂点集合に頂点vを追加
                    bc_idx[v] = idx
            idx += 1
        return bc, bc_idx, bc_tree, num_ap, bce, bcv, is_ap

#####################################################

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
x = LowLink(G)
x.build()
for i, xi in enumerate(x.biconnected_component()[-1]):
    if xi: print(i)

# https://kntychance.hatenablog.jp/entry/2022/09/16/161858
# n = 10
# m = 12
# edge = [(0,1), (1,2), (2,3), (2,4), (2,5), (1,5), (1,6), (1,8), (6,7), (6,8), (0,9), (8,9)]
# G = [[] for _ in range(n)]
# for _ in range(m):
#     # a, b = map(int, input().split())
#     # a -= 1; b -= 1
#     G[a].append(b)
#     G[b].append(a)
# for gi in G:
#     gi.sort(reverse=True)

# x = LowLink(G)
# x.build()
# print(x.ord)
# print(x.son)
# print(x.low)
#print(x.bridges)
#print(x.two_edge_connected_component())
# print(x.biconnected_component())

######prefix######
# Lib_G_グラフ橋関節_lowlink
##############end##############
