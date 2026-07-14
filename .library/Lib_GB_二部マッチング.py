##############name##############
# Graph二部マッチング
######description######
# Graph二部マッチング
######body######

from collections import deque

##二部マッチング

class BipartileMatching:
    ##L2R:Lから見たRのマッチングを記録
    ##R2L:Rから見たLのマッチングを記録
    ##backpath:L側に逆辺が張られている場合の辿る先
    ##root:逆辺を考慮したLの始点を記録

    def __init__(self, L, R):
        self.L = L
        self.R = R
        self.G = [[] for _ in range(L)]
        self.L2R = None
        self.R2L = None

    def add_edge(self, u, v):
        self.G[u].append(v)

    @property
    def matching(self):
        L = self.L
        R = self.R
        L2R = [-1] * L
        R2L = [-1] * R
        backpath = [-1] * L
        root = [-1] * L
        res, f = 0, True
        while f:
            f = False
            q=deque()
            for i in range(L):
                ##まだマッチング対象が見つかっていなければ
                ##iを始点としてキューに追加
                if L2R[i] == -1:
                    root[i] = i
                    q.append(i)

            while q:
                s = q.popleft()
                ##逆辺を辿った先のrootが-1になっていればcontinue
                if ~L2R[root[s]]: continue

                ##始点から接続されている辺を全探索する
                for t in self.G[s]:
                    if R2L[t] == -1:
                        ##逆辺が存在する場合は辿っていく
                        while t != -1:
                            R2L[t] = s
                            L2R[s], t = t , L2R[s]
                            s = backpath[s]
                        f = True
                        res += 1
                        break

                    ##仮のtに対するマッチング候補の情報を更新しキューに追加する
                    temps = R2L[t]
                    if ~backpath[temps]: continue
                    backpath[temps] = s
                    root[temps] = root[s]
                    q.append(temps)

            ##更新があれば逆辺・始点情報を初期化する
            if f:
                backpath = [-1] * L
                root = [-1] * L
        self.L2R = L2R
        self.R2L = R2L
        return res

#################################
n, m, e = map(int, input().split())
BM = BipartileMatching(n, m)
for i in range(e):
    x, y = map(int, input().split())
    BM.add_edge(x, y)
print(BM.matching)

######prefix######
# Lib_G_二部マッチング_bipartitematching
##############end##############
