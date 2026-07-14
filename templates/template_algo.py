import sys

sys.setrecursionlimit(1000_000_000)

G = [[] for _ in range({1: N})]
for _ in range({1: M}):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, w))
    G[b].append((a, w))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b, w = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((b, w))
        G[b].append((a, w))
