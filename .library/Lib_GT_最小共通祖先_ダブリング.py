##############name##############
# LCA
######description######
# 最小共通祖先
######body######


class LCA:
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

    def __init__(self, n: int, G: list[list[int]], r: int) -> None:
        self.n: int = n
        self.root: int = r
        self.edges: list[list[int]] = G
        self.lv: int = n.bit_length()
        self.parent: list[list[int]] = [[-1] * n for _ in range(self.lv)]
        self.depth: list[int] = [-1] * n
        self._build()

    def _build(self) -> None:
        """深さと親の設定とダブリング"""
        # 深さと親の設定
        r: int = self.root
        depth = self.depth
        parent = self.parent
        # que: deque[int] = deque([r])
        que = [r]
        depth[r], parent[0][r] = 0, r
        while que:
            cur = que.pop()
            dep: int = depth[cur]
            for nxt in self.edges[cur]:
                if depth[nxt] != -1:
                    continue
                depth[nxt] = dep + 1
                parent[0][nxt] = cur
                que.append(nxt)
        # ダブリング
        for k in range(1, self.lv):
            pk = parent[k]
            pm = parent[k - 1]
            for v in range(self.n):
                pk[v] = pm[pm[v]]

    def lca(self, u: int, v: int) -> int:
        """
        u, v の最小共通祖先を返す
        """
        parent = self.parent
        depth = self.depth
        # u,vの高さを合わせる
        if depth[u] < depth[v]:
            u, v = v, u

        diff = depth[u] - depth[v]
        k = 0
        while diff:
            if diff & 1:
                u = parent[k][u]
            diff >>= 1
            k += 1

        if u == v:
            return u
        # u, vのギリギリ合わない高さまで昇る
        for k in range(self.lv - 1, -1, -1):
            if parent[k][u] != parent[k][v]:
                u = parent[k][u]
                v = parent[k][v]
        return parent[0][u]

    def distance(self, u: int, v: int) -> int:
        """
        u, v の距離を返す
        """
        depth = self.depth
        lca = self.lca(u, v)
        return depth[u] + depth[v] - 2 * depth[lca]

    def la(self, x: int, h: int) -> int:
        """h代前祖先"""
        parent = self.parent

        k = 0
        while h:
            if h & 1:
                x = parent[k][x]
            h >>= 1
            k += 1

        return x

    def jump(self, u: int, v: int, kth: int) -> int:
        """
        u -> v のパス上で
        u を 0 番目とした kth 頂点
        """
        _lca = self.lca(u, v)
        du = self.depth[u]
        dv = self.depth[v]
        dlca = self.depth[_lca]

        path_len = du - dlca + dv - dlca
        if kth < 0 or path_len < kth:
            return -1

        if du - dlca >= kth:
            return self.la(u, kth)

        return self.la(v, path_len - kth)


########################################

# N, Q = map(int, input().split())
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

lca = LCA(N, G, 0)
Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    # u, v, k = map(int, input().split())
    u -= 1
    v -= 1
    # print(lca.jump(u, v, k))
    print(lca.distance(u, v) + 1)

######prefix######
# Lib_GT_最小共通祖先_LCA
##############end##############
