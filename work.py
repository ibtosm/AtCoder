import sys
from collections import deque

sys.setrecursionlimit(1000_000_000)


def _bfs(n, G, root=0):
    """ルートからBFS、最後に訪れたノードが最遠となる"""
    _depth: list[int] = [-1] * n
    q: deque[int] = deque()
    q.append(root)
    _depth[root] = 0
    _parent: list[int] = [-1] * n
    farthest_node: int = root
    while q:
        cur: int = q.popleft()
        dep: int = _depth[cur]
        for nxt in G[cur]:
            if _depth[nxt] != -1:
                continue
            q.append(nxt)
            newdep: int = dep + 1
            _depth[nxt] = newdep
            _parent[nxt] = cur
            farthest_node = nxt
    return farthest_node, _depth[farthest_node], _depth, _parent


def tree_diameter(n, G) -> tuple[int, int, int, list[int], list[int]]:
    """u, v:直径のノード二組"""
    """diam:直径の長さ"""
    """depth:uからのノードの深さ"""
    """parent:uからの木のノードの親"""
    u, *_ = _bfs(n, G, root=0)
    v, diam, depth, parent = _bfs(n, G, root=u)
    return u, v, diam, depth, parent


def tree_heights(n, G):
    """各頂点から最遠頂点までの距離"""
    u, *_ = _bfs(n, G, root=0)
    v, _, depthu, _ = _bfs(n, G, root=u)
    _, __, depthv, __ = _bfs(n, G, root=v)
    return [max(x, y) for x, y in zip(depthu, depthv)]


def tree_centre(n, G) -> tuple[int, tuple[int, int]]:
    """木の中心"""
    """diam:直径の長さ"""
    """centre:中心のノード"""
    """直径が偶数の時、１つに決まる,奇数の時、２つ"""
    _, _v, diam, _depth, _parent = tree_diameter(n, G)

    halfdist: int = diam // 2
    centre: int = _v
    while diam - _depth[centre] < halfdist:
        # 葉から根に向かって半径分辿る
        centre = _parent[centre]

    centres: tuple[int, int] = (_parent[centre] if diam % 2 else centre, centre)

    return diam, centres


def count_diameter(n, G):
    """cntは中心からの各部分木の(ノード数, 最遠葉)
    countは直径の本数
    """

    diam, (cu, cv) = tree_centre(n, G)

    radius: int = diam // 2

    def _dfs_1(x, p, d):
        nodecount = 1
        farthestleaf = d == radius
        for nx in G[x]:
            if nx == p:
                continue
            u, v = _dfs_1(nx, x, d + 1)
            nodecount += u
            farthestleaf += v
        return nodecount, farthestleaf

    cnt: list[tuple[int, int]] = []
    if cu == cv:
        for nx in G[cu]:
            cnt.append(_dfs_1(nx, cu, 1))
    else:
        cnt.append(_dfs_1(cu, cv, 0))
        cnt.append(_dfs_1(cv, cu, 0))

    sig, count = 0, 0
    for _, ci in cnt:
        count += sig * ci
        sig += ci
    return (cu, cv), count


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
