####################
# EDPC G Longest Path
# https://atcoder.jp/contests/dp/tasks/dp_g/
####################

# トポロジカルソート
# 有向非巡回グラフ（DAG）の各ノードを順序付けして、どのノードもその出力辺の先のノードより前にくるように並べることである。
# 有向非巡回グラフは必ずトポロジカルソートすることができる。


from collections import deque

class topological_sort:
    def __init__(self, n:int) -> None:
        self.n = n
        self.in_cnt = [0] * n   # 入力
        self.ts = []            # トポロジカルソート
        self.parents = [-1] * n # 親 -1は根
        self.edges = [[] for _ in range(n)] # 辺
        self.node_zero = []     # ゼロ次のノード

    def add_edge(self, fm:int, to:int) -> None:
        self.edges[fm].append(to)
        self.in_cnt[to] += 1

    def build(self) -> None:
        self.node_zero = [i for i in range(self.n) if self.in_cnt[i]==0]
        q = deque(self.node_zero)
        while q:
            p = q.popleft()
            self.ts.append(p)
            for nxt in self.edges[p]:
                self.in_cnt[nxt] -= 1
                if self.in_cnt[nxt] == 0:
                    q.append(nxt)
                    self.parents[nxt] = p

    def is_dag(self) -> bool:
        return len(self.ts)==self.n
        # True 閉路なしDAG
        # False 閉路あり

#########################################

n, m = map(int, input().split())
ts = topological_sort(n)
# 隣接リストの作成
for i in range(m):
    # a->b 有向辺
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ts.add_edge(a, b)

ts.build()

dp = [0] * n

prev = 0
for i in ts.ts:
    if ts.parents[i] == -1:
        continue
    dp[i] = dp[ts.parents[i]] + 1

print(max(dp))
