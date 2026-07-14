# ####################
# EDPC V Subtree
# https://atcoder.jp/contests/dp/tasks/dp_v
####################
# 全方位木DP


from collections import deque

class Tree():
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.root = None    # 根
        self.size = [1] * n # 部分木のノード数
        self.depth = [-1] * self.n
        self.par = [-1] * self.n
        self.order = [] # 深さ優先探索の行きがけ順

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def set_root(self, root):
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
        for p in self.order[::-1]:
            for q in self.edges[p]:
                if self.par[p] == q: continue
                self.size[p] += self.size[q]

    def rerooting(self, op, merge, id):
        dp = [id] * self.n          # 部分木の情報
        dp2 = [id] * self.n         # 親の部分木
        left = [id] * self.n
        right = [id] * self.n

        for p in self.order[::-1]:
            tmp = id
            for q in self.edges[p]:
                if self.par[p] == q: continue
                left[q] = tmp
                tmp = merge(tmp, op(dp[q], p, q))
            tmp = id
            for q in self.edges[p][::-1]:
                if self.par[p] == q: continue
                right[q] = tmp
                tmp = merge(tmp, op(dp[q], p, q))
            dp[p] = tmp
        for q in self.order[1:]:
            pq = self.par[q]
            dp2[q] = merge(left[q], right[q])
            dp2[q] = op(merge(dp2[q], dp2[pq]), q, pq)
            dp[q] = merge(dp[q], dp2[q])
        return dp

#######################################################
# a, bはdpの値, uは親, vは子
op = lambda a, u, v: a + 1 # dpをmergeする前にする作業
merge = lambda a, b: a * b % m # dpをmerge
id = 1  # mergeの単位元
#
#######################################################
n, m = map(int, input().split())
T = Tree(n)
for _ in range(n-1):
    a, b = map(int, input().split())
    T.add_edge(a-1, b-1)

T.set_root(0)
dp = T.rerooting(op, merge, id)
print("\n".join(map(str, dp)))
