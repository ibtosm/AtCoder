####################
# EDPC R Walks
# https://atcoder.jp/contests/dp/tasks/dp_r/
####################
# 行列演算による


import sys
def input(): return sys.stdin.readline().rstrip()

mod = 1000000007

# 行列

def prod(ma, mb, mod = 10**9+7):
    n = len(ma)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] += ma[i][k]*mb[k][j]
                ret[i][j] %= mod
    return ret

def powmat(ma, k, mod = 10**9+7):
    n = len(ma)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        ret[i][i] = 1
    for _ in range(k):
        if k & 1:
            ret = prod(ret, ma, mod)
        ma = prod(ma, ma, mod)
        k >>= 1
        if k == 0: break
    return ret


n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
print(sum(sum(x)%mod for x in powmat(A, k))%mod)
