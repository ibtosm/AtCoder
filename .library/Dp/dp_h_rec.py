####################
# EDPC H Grid1
# https://atcoder.jp/contests/dp/tasks/dp_h/
####################
import sys
from functools import lru_cache

def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
mod = 1000000007
h, w = map(int, input().split())
grid = [input() for _ in range(h)]



@lru_cache(maxsize=1000000)
def dfs(i, j):
    if i == 0 and j == 0:
        return 1
    if i < 0 or i >= h:
        return 0
    if j < 0 or j >= w:
        return 0
    if grid[i][j] == '#':
        return 0
    return (dfs(i-1, j) + dfs(i, j-1)) % mod

print(dfs(h-1, w-1))
