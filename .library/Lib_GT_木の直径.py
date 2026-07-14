##############name##############
# Diameter
######description######
# 木の直径
######body######

from collections import deque


def _bfs(n, G, root=0):
    _depth = [None] * n
    q = deque()
    q.append(root)
    _depth[root] = 0
    _parent = [None] * n
    farthest_node = root
    while q:
        cur = q.popleft()
        dep = _depth[cur]
        for nxt in G[cur]:
            if _depth[nxt] is not None:
                continue
            q.append(nxt)
            newdep = dep + 1
            _depth[nxt] = newdep
            _parent[nxt] = cur
            farthest_node = nxt
    return farthest_node, _depth[farthest_node], _depth, _parent


def tree_diameter(n, G):
    u, *_ = _bfs(n, G, 0)
    v, diam, depth, parent = _bfs(n, G, u)
    return u, v, diam, depth, parent


def tree_heights(n, G):
    u, *_ = _bfs(n, G, 0)
    v, _, depthu, _ = _bfs(n, G, u)
    _, __, depthv, __ = _bfs(n, G, v)
    return [max(x, y) for x, y in zip(depthu, depthv)]


def tree_centre(n, G):
    """木の中心"""
    u, v, diam, depth, parent = tree_diameter(n, G)
    hd = diam // 2
    centre = v
    while diam - depth[centre] < hd:
        centre = parent[centre]
    if diam % 2 == 0:
        return u, v, diam, (centre, centre)
    else:
        return u, v, diam, (parent[centre], centre)


def count_diameter(n, G):
    """cntは中心からの各部分木の(ノード数, 最遠葉)

    countは直径の本数
    """

    def dfs(x, p, d, r):
        nodecount = 1
        farthestleaf = d == r
        for nx in G[x]:
            if nx == p:
                continue
            u, v = dfs(nx, x, d + 1, r)
            nodecount += u
            farthestleaf += v
        return nodecount, farthestleaf

    _, _, diam, (cu, cv) = tree_centre(n, G)

    r = diam // 2
    cnt = []
    if cu == cv:
        for nx in G[cu]:
            cnt.append(dfs(nx, cu, 1, r))
    else:
        cnt.append(dfs(cu, cv, 0, r))
        cnt.append(dfs(cv, cu, 0, r))

    sig, sig2 = 0, 0
    for _, ci in cnt:
        sig += ci
        sig2 += ci * ci
    count = sig * sig - sig2
    count //= 2
    return (cu, cv), count


##############################

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

print(tree_diameter(n, G))
print("-------------------")
print(tree_heights(n, G))
print("-------------------")
print(tree_centre(n, G))
print("-------------------")
print(count_diameter(n, G))


######prefix######
# Lib_GT_木の直径
##############end##############
