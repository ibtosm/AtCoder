####################
# EDPC Y - Grid2
# https://atcoder.jp/contests/dp/tasks/dp_y/
####################
# グリッド計算
# 行けないところを控除する方法
# 初めて到達する場合からの場合分け


import sys
from operator import itemgetter
def input(): return sys.stdin.readline().rstrip()

class Combination:
    def __init__(self, mod=10**9+7, max_n=1):
        self.mod = mod
        self.max_n = 1
        self.factorial = [1, 1]
        self.inverse = [None, 1]
        self.f_inverse = [1, 1]
        self.__preprocessing(max_n)


    def __preprocessing(self, max_n):
        fac = self.factorial
        inv = self.inverse
        finv = self.f_inverse
        mod = self.mod
        fac += [-1] * (max_n - self.max_n)
        inv += [-1] * (max_n - self.max_n)
        finv += [-1] * (max_n - self.max_n)
        for i in range(self.max_n + 1, max_n + 1):
            fac[i] = fac[i - 1] * i % mod
            inv[i] = mod - inv[mod % i] * (mod // i) % mod
            finv[i] = finv[i - 1] * inv[i] % mod
        self.max_n = max_n


    def fac(self, n):
        if n < 0:
            return 0
        if n > self.max_n: self.__preprocessing(n)
        return self.factorial[n]


    def nCr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        if n > self.max_n: self.__preprocessing(n)
        return self.factorial[n] * (self.f_inverse[r] * self.f_inverse[n - r] % self.mod) % self.mod
dp

    def nPr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        if n > self.max_n: self.__preprocessing(n)
        return self.factorial[n] * self.f_inverse[n - r] % self.mod


################################

mod = 1000000007
h, w, n = map(int, input().split())

walls = [(h-1, w-1)]
for _ in range(n):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    walls.append((r, c))
walls.sort(key=itemgetter(1))
walls.sort(key=itemgetter(0))

CMB = Combination(mod, 10**6)

# dp[i]
# i番目に初めて到着する組み合わせ

n = len(walls)
dp = [0] * n

for i in range(n):
    hi, wi = walls[i]
    dpi = CMB.nCr(hi+wi, hi)
    for j in range(i):
        hj, wj = walls[j]
        dpi -= dp[j] * CMB.nCr(hi+wi-hj-wj, hi-hj)
        dpi %= mod
    dp[i] = dpi

print(dp[n-1])
