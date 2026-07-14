##############name##############
# LCA
######description######
# 最小共通祖先
######body######
from collections import deque
class Lca:
    """Lowest Common Ancestor

    u, vの共通の親
    ダブリング p[i][v] = vの2^i個 親

    Parameters
    ----------
    n : int
        nodeの数
    G : graph
    r : root
    """
    def __init__(self, n: int, G, r:int) -> None:
        self.n = n
        self.root = r
        self.edges = G
        self.lv = n.bit_length()
        self.p = [[None] * n for _ in range(self.lv)]
        self.maxcost = [[0] * n for _ in range(self.lv)]
        self._depth = [None] * n
        self._costs = [None] * n
        self.memodist = dict()
        self.memocost = dict()
        self.build()

    def build(self):
        """深さと親の設定とダブリング
        """
        # 深さと親の設定
        r = self.root
        q = deque([r])
        self._depth[r], self._costs[r], self.p[0][r], self.maxcost[0][r] = 0, 0, r, 0
        while q:
            cur = q.popleft()
            dep = self._depth[cur]
            dis = self._costs[cur]
            for nxt in self.edges[cur]:
                if type(nxt) != int:
                    nxt, cost = nxt
                else:
                    cost = 1
                if self.p[0][nxt] != None: continue
                q.append(nxt)
                self._depth[nxt], self._costs[nxt], self.p[0][nxt], self.maxcost[0][nxt] = dep + 1, dis + cost, cur, cost
        # ダブリング
        for i in range(1, self.lv):
            for v in range(self.n):
                nv = self.p[i-1][v]
                self.p[i][v] = self.p[i-1][nv]
                self.maxcost[i][v] = max(self.maxcost[i-1][v], self.maxcost[i-1][nv])


    def _lca(self, u, v):
        """共通祖先, 最大辺
        Parameters
        ----------
        u, v : node
            ノード
        Returns
        -------
        int, int
            共通祖先のノード, 最大辺
        """
        _max_cost = 0
        # u,vの高さを合わせる
        if self._depth[u] < self._depth[v]: u, v = v, u
        for i in range(self.lv):
            if self._depth[u] - self._depth[v] >> i & 1:
                _max_cost = max(_max_cost, self.maxcost[i][u])
                u = self.p[i][u]
        if u == v: return u, _max_cost
        # u, vのギリギリ合わない高さまで昇る
        for i in range(self.lv)[::-1]:
            if self.p[i][u] != self.p[i][v]:
                _max_cost = max(_max_cost, self.maxcost[i][u], self.maxcost[i][v])
                u = self.p[i][u]
                v = self.p[i][v]
        return self.p[0][u], max(_max_cost, self.maxcost[0][u], self.maxcost[0][v])


    def lca(self, u, v):
        return self._lca(u, v)[0]


    def max_cost(self, u, v):
        return self._lca(u, v)[1]


    def distance(self, u, v):
        if not (u, v) in self.memodist:
            lca = self.lca(u, v)
            self.memodist[(u, v)] = self._depth[u] + self._depth[v] - 2 * self._depth[lca]
        return self.memodist[(u, v)]


    def cost(self, u, v):
        if not (u, v) in self.memocost:
            lca = self.lca(u, v)
            self.memocost[(u, v)] = self._costs[u] + self._costs[v] - 2 * self._costs[lca]
        return self.memocost[(u, v)]


    def _la(self, x, h):
        """h代前祖先
        """
        for i in range(self.lv)[::-1]:
            if h >= 1 << i:
                x = self.p[i][x]
                h -= 1 << i
        return x


    def jump(self, u, v, i):
        """
        u -> vへのパスのk番目の頂点
        """
        c = self.lca(u, v)
        du = self._depth[u]
        dv = self._depth[v]
        dc = self._depth[c]

        path_len = du - dc + dv - dc
        if path_len < i:
            return -1

        if du - dc >= i:
            return self._la(u, i)

        return self._la(v, path_len - i)

########################################

# n, q = map(int, input().split())
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

lca = Lca(n, G, 0)
q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    # u, v, k = map(int, input().split())
    # print(lca.jump(u, v, k))
    print(lca.distance(u, v)+1)

######prefix######
# Lib_GT_最小共通祖先_LCA
##############end##############
