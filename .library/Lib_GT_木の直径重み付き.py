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
    farthest_dist = 0
    farthest_node = 0
    while q:
        cur = q.popleft()
        dep = _depth[cur]
        for nxt in G[cur]:
            nx, cost = nxt
            if _depth[nx] is not None:
                continue
            q.append(nx)
            newdep = dep + cost
            _depth[nx] = newdep
            if newdep > farthest_dist:
                farthest_dist = newdep
                farthest_node = nx
    return farthest_node, farthest_dist, _depth, _parent


def tree_diameter(n, G):
    u, *_ = _bfs(n, G, 0)
    v, diam, depth, parent = _bfs(n, G, u)
    return u, v, diam, depth, parent


def tree_heights(n, G):
    u, *_ = _bfs(n, G, 0)
    v, _, depthu, _ = _bfs(n, G, u)
    _, __, depthv, __ = _bfs(n, G, v)
    return [max(x, y) for x, y in zip(depthu, depthv)]


##############################

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, w))
    G[b].append((a, w))

print(tree_diameter(n, G))
print(tree_heights(n, G))


######prefix######
# Lib_GT_木の直径
##############end##############
