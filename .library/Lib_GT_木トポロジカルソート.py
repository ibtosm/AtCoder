##############name##############
# トポロジカルソート木
######description######
# 木トポロジカルソート topologicalsort
######body######
# トポロジカルソート
# 有向非巡回グラフ（DAG）の各ノードを順序付けして、どのノードもその出力辺の先のノードより前にくるように並べることである。
# 有向非巡回グラフは必ずトポロジカルソートすることができる。
from collections import deque

class topological_sort:
    def __init__(self, n:int, G) -> None:
        self.n = n
        self.ts = []            # トポロジカルソート
        self.parents = [-1] * n # 親 -1は根
        self.G = G              # 辺
        self.childrens = G.copy() # 辺


    def build(self, root):
        que = deque([root])
        self.ts = []            # トポロジカルソート
        while que:
            x = que.popleft()
            self.ts.append(x)
            for nx in self.G[x]:
                if nx == self.parents[x]: continue
                self.parents[nx] = x
                self.childrens[nx].remove(x)
                que.append(nx)

#########################################
# n, m = map(int, input().split())
n = int(input())
G = [[] for _ in range(n)]
m = n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    w = 0
    G[a].append((b, w))

ts = topological_sort(n, G)

ts.build(0)

print(ts.ts)
print(ts.parents)

# 木dp  #ノードに1を置いて葉から合計する
dp = [1] * n
for i in ts.ts[::-1]:  #葉から
    for j in ts.childrens[i]:
        dp[i] += dp[j]


######prefix######
# Lib_GT_木トポロジカルソート_topologicalsort
##############end##############
