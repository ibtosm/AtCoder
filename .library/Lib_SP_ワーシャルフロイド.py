######title######
# ワーシャルフロイド法
######subtitle######
# warshall_floyd: 全頂点間最短経路のリストを作る
# O(N^3)

##############name##############
# ワーシャルフロイド法
#discription#
# 全頂点間最短路
# d[i][j]は2頂点間i, j間の移動コストを格納, Nは頂点数
# O(N^3)
######body######

class WarshallFloyd:
    INF = 10**18
    directed = False    # 無向: False   有向: True
    def __init__(self, n:int) -> None:
        self.n = n
        self.dist = [[self.INF] * n for _ in range(n)]
        for i in range(n):
            self.dist[i][i] = 0


    def add_edge(self, fm: int, to: int, cost: int):
        """辺の追加"""
        if self.dist[fm][to] <= cost: return
        self.dist[fm][to] = cost
        if self.directed: return
        self.dist[to][fm] = cost

    def build(self):
        if self.directed:
            self._build_directed()
        else:
            self._build_nodirected()


    def _build_directed(self):
        """O(N^3)計算"""
        n = self.n
        dist = self.dist
        for k in range(n):
            for i in range(n):
                if dist[i][k] == self.INF: continue
                for j in range(i):
                    if dist[k][j] == self.INF: continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    dist[j][i] = dist[i][j]
        self.dist = dist

    def _build_nodirected(self):
        """O(N^3)計算"""
        n = self.n
        dist = self.dist
        for k in range(n):
            for i in range(n):
                if dist[i][k] == self.INF: continue
                for j in range(n):
                    if dist[k][j] == self.INF: continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        self.dist = dist


    def update_edge(self, fm, to, cost):
        """特定の辺を更新"""
        dist = self.dist
        if dist[fm][to] <= cost:
            return
        dist[fm][to] = cost
        if not self.directed:
            dist[to][fm] = cost
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][fm] + cost + dist[to][j])
                if not self.directed:
                    dist[i][j] = min(dist[i][j], dist[i][to] + cost + dist[fm][j])
        self.dist = dist


    @property
    def is_neg_cycle(self) -> bool:
        """負値閉路検索"""
        for i in range(self.n):
            if self.wf[i][i] < 0:
                return True
        return False


    def path(self, s: int, g: int):
        """経路復元"""
        ret = []
        if s == g or self.wf[s][g] == self.INF:
            return ret
        cur = s
        while cur!=g:
            for nxt in range(self.n):
                if nxt==cur or nxt==s: continue
                if self.d[cur][nxt] + self.wf[nxt][g] == self.wf[cur][g]:
                    ret.append((cur, nxt))
    #                ret.append((nxt, cur))
                    cur = nxt
                    break
        return ret

##############################

n, m = map(int,input().split()) #N:頂点数 m:辺の数

wf = WarshallFloyd(n)

for _ in range(m):
    u, v, w = map(int,input().split())
    u -= 1; v -= 1
    wf.add_edge(u, v, w)
#    wf.add_edge(v, u, w)

wf.build()

print(wf.path(0, n-1))

######prefix######
# Lib_SP_最短経路探索_warshall
##############end##############
