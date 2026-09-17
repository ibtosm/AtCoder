from atcoder.dsu import DSU


class Kruskal:
    def __init__(self, n: int, G: list) -> None:
        self.n = n
        self.all_edges = G
        self.edges = [False] * len(G)
        self.G = [[] for _ in range(n)]
        self.weight = 0
        self.nodes = set([])
        self.INF = 10**20
        self.build()

    def build(self) -> None:
        uf = DSU(self.n)
        for u, v, w, i in sorted(
            [(a, b, w, i) for i, (a, b, w) in enumerate(self.all_edges)],
            key=lambda x: x[2],
        ):
            if not uf.same(u, v):
                uf.merge(u, v)
                self.weight += w
                self.nodes |= {u, v}
                self.edges[i] = True
                self.G[u].append((v, w))
                self.G[v].append((u, w))
        if sum(self.edges) != self.n - 1:  #
            self.weight = self.INF


################################

n, m = map(int, input().split())

# 辺リストの作成
G = []
for i in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    G.append((a, b, w))

mst = Kruskal(n, G)
print(mst.weight)
