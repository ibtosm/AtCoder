

import sys
def input(): return sys.stdin.readline().rstrip()

class RMQRAQ:
    def __init__(self, a:list) -> None:

    # N: 処理する区間の長さ
        self.INF = 0
        self.log = (len(a)-1).bit_length()
        self.size = 1 << self.log
        self.data = [0] * (2*self.size)
        self.lazy = [0] * (2*self.size)
        for i, ai in enumerate(a):
            self.data[i + self.size] = ai


    def gindex(self, l, r):
        L = (l + self.size) >> 1; R = (r + self.size) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range(self.log):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1; R >>= 1

    # 遅延伝搬処理
    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if not v:
                continue
            self.lazy[2*i-1] += v; self.lazy[2*i] += v  # Add
            self.data[2*i-1] += v; self.data[2*i] += v  # Add
            self.lazy[i-1] = 0

    # 区間[l, r)にxを加算
    def update(self, l, r, x):
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        L = self.size + l; R = self.size + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] += x; self.data[R-1] += x    # Add
            if L & 1:
                self.lazy[L-1] += x; self.data[L-1] += x    # Add
                L += 1
            L >>= 1; R >>= 1
        for i in ids:
            self.data[i-1] = min(self.data[2*i-1], self.data[2*i])  # Min

    # 区間[l, r)内の最小値を求める
    def query(self, l, r):
        self.propagates(*self.gindex(l, r))
        L = self.size + l; R = self.size + r

        s = self.INF
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])  # Min
            if L & 1:
                s = min(s, self.data[L-1])  # Min
                L += 1
            L >>= 1; R >>= 1
        return s

#######################################################

n, m = map(int, input().split())
intvls = [[] for i in range(n+1)]
for _ in range(m):
    l, r, a = map(int, input().split())
    intvls[r-1].append((l-1, -a))

# dp[i][j]  i番目まで見て文字確定していて,i番目が1
sgt = RMQRAQ([0] * n)

for r in range(n):
    mx = sgt.query(0, r)
    sgt.update(r, r+1, mx)
    for l, a in intvls[r]:
        sgt.update(l, r+1, a)

print(max(0, -sgt.query(0, n)))
