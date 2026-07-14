##############name##############
# Graph最遠パス
######description######
# Graph最遠パス
######body######

# root から始めて一番遠いところにあるノードを見つける
from collections import deque
def bfs(n, G, root=0, cost=1):
    _depth = [None] * n
    q = deque()
    q.append(root)
    _depth[root] = 0
    _parent = [-1] * n
    farest_dist = -1
    while q:
        cur = q.popleft()
        dep = _depth[cur]
        for nxt in G[cur]:
            if type(nxt) != int: nxt, cost = nxt
            if _depth[nxt] != None: continue
            newdep = dep + cost
            q.append(nxt)
            _parent[nxt] = cur
            _depth[nxt] = newdep
            if newdep > farest_dist:
                farest_dist = newdep
                farest_node = nxt
    return farest_node, farest_dist, _depth


##############################


n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    G[a].append((b, w))
    G[b].append((a, w))



######prefix######
# Lib_G_最短パス
##############end##############
