##############name##############
# 全方位木DP
######description######
# 全方位木DP
# https://algo-logic.info/tree-dp/
######body######

from collections import deque

class Tree:
    def __init__(self, n, E):
        self.n = n
        self.root = None    # 根
        self.depth = None   # 深さ
        self.par = None     # 親
        self.order = None   # 深さ優先探索の行きがけ順
        self.dp = None
        self.dp1 = None
        self.edges = [[] for _ in range(n)]
        for a, b in E:
            self.edges[a].append(b)
            self.edges[b].append(a)


    def set_root(self, root):
        self.depth = [-1] * self.n
        self.par = [-1] * self.n
        self.order = []
        self.root = root
        self.depth[root] = 0
        self.order.append(root)
        nxt_q = deque([root])
        while nxt_q:
            p = nxt_q.pop() # 深さ優先探索
            for q in self.edges[p]:
                if self.depth[q] != -1: continue
                self.par[q] = p
                self.depth[q] = self.depth[p] + 1
                self.order.append(q)
                nxt_q.append(q)
        # self.size = [1] * n # 部分木のノード数
        # for p in self.order[::-1]:
        #     for q in self.edges[p]:
        #         if self.par[p] == q: continue
        #         self.size[p] += self.size[q]

    def rerooting(self, merge, op, fin, id):
        if self.root == None: self.set_root(0)
        dp1 = [id] * self.n
        dp2 = [id] * self.n
        for p in self.order[::-1]:
            t = id
            for q in self.edges[p]:
                if self.par[p] == q: continue
                dp2[q] = t
                t = merge(t, op(dp1[q], p, q))
            t = id
            for q in self.edges[p][::-1]:
                if self.par[p] == q: continue
                dp2[q] = merge(t, dp2[q])
                t = merge(t, op(dp1[q], p, q))
            dp1[p] = t
        self.dp1 = dp1[:]
        for q in self.order[1:]:
            pq = self.par[q]
            dp2[q] = op(merge(dp2[q], dp2[pq]), q, pq)
            dp1[q] = merge(dp1[q], dp2[q])
        for q in self.order:
            pq = self.par[q]
            dp1[q] = fin(dp1[q], pq, q)
        self.dp = dp1[:]
        return dp1


#####################################
# a, bはdpの値, pは考察している辺の親, qは子
# merge: dpをmerge
# op: dpをmerge前にする作業
# fin: dpをmerge後にする作業
# ie: mergeの単位元
#####################################


#######################################################
# https://atcoder.jp/contests/abc160/tasks/abc160_f

n = int(input())
E = [tuple(map(lambda x: int(x)-1 , input().split())) for _ in range(n-1)]
T = Tree(n, E)

mod, lim = 1000000007, n + 1
g1, g2 = [[1]*(lim+1) for _ in range(2)]
for i in range(2, lim + 1):
    g1[i] = g1[i-1] * i % mod
g2[-1] = pow(g1[-1], mod-2, mod)
for i in range(lim, 0, -1):
    g2[i-1] = g2[i] * i % mod

def fac(n): return g1[n]
def facinv(n): return g2[n]

merge = lambda a, b: (a[0] * b[0] * facinv(a[1]) * facinv(b[1]) * fac(a[1]+b[1]) % mod, (a[1] + b[1]) % mod)
op = lambda a, p, q: (a[0], (a[1] + 1) %mod)
fin = lambda a, p, q: a
id = (1, 0)

ret = [dpi[0] for dpi in T.rerooting(merge, op, fin, id)]
print("\n".join(map(str, ret)))


#######################################################
# https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_d

n = int(input())
E = [tuple(map(lambda x: int(x)-1 , input().split())) for _ in range(n-1)]
T = Tree(n, E)
# a, bはdpの値, pは考察している接点親, qは子
# dpをmerge
merge = lambda a, b: a + b
# dpをmerge前にする作業
op = lambda a, p, q: a / (len(T.edges[q])-1) + 1 if a != 0 else 1
# dpをmerge後にする作業
fin = lambda a, p, q: a / len(T.edges[q])
# mergeの単位元
id = 0

ret = T.rerooting(merge, op, fin, id)
print("\n".join(map(str, ret)))

#######################################################
# https://atcoder.jp/contests/abc222/tasks/abc222_f

n = int(input())
E = []
cost = {}
for _ in range(n-1):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    E.append((a, b))
    cost[(a, b)] = c
    cost[(b, a)] = c
D = list(map(int, input().split()))

T = Tree(n, E)

merge = lambda a, b: max(a, b)
# dpをmerge前にする作業
op = lambda a, p, q: max(a, D[q]) + cost[(p, q)]
# dpをmerge後にする作業
fin = lambda a, p, q: a
# mergeの単位元
id = 0

ret = T.rerooting(merge, op, fin, id)
print("\n".join(map(str, ret)))


#######################################################
# https://atcoder.jp/contests/abc348/tasks/abc348_e

n = int(input())
E = [tuple(map(lambda x: int(x)-1 , input().split())) for _ in range(n-1)]
C = list(map(int, input().split()))
T = Tree(n, E)

# a, bはdpの値, pは考察している接点親, qは子
# dpをmerge
merge = lambda a, b:  (a[0]+b[0], a[1]+b[1])
# dpをmerge前にする作業
op = lambda a, p, q: (a[0] + C[q], a[0] + a[1] + C[q])
# dpをmerge後にする作業
fin = lambda a, p, q: a
# mergeの単位元
id = (0, 0)

ret = min(dpi[1] for dpi in T.rerooting(merge, op, fin , id))
print(ret)

#######################################################


######prefix######
# Lib_GT_全方位木DP
##############end##############
