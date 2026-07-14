####################
# EDPC Z - Frog 3
# https://atcoder.jp/contests/dp/tasks/dp_z/
####################
# Covex Hull Trickを使う

class CHT:
    def __init__(self, X:list) -> None:
        X = sorted(list(set(X)))
        self.inf = 10 ** 18
        self.n = 1 << (len(X) - 1).bit_length()
        self.X = X + [self.inf] * (self.n - len(X))
        self.D = {a: i for i, a in enumerate(X)}
        self.lmr = [(0, 0, 0)] * self.n + [(x, x, x) for x in self.X]
        for i in range(1, self.n)[::-1]:
            self.lmr[i] = (self.lmr[i*2][0], self.lmr[i*2][2], self.lmr[i*2^1][2])
        self.F = [None] * (self.n * 2)


    def calc(self, f:tuple, x:int) -> int:
        a, b = f
        return a * x + b


    def _update(self, i, f):
        while True:
            l, m, r = self.lmr[i]
            fi = self.F[i]
            if fi is None:
                self.F[i] = f
                return
            cl = self.calc(fi, l) > self.calc(f, l)
            cr = self.calc(fi, r) > self.calc(f, r)
            cm = self.calc(fi, m) > self.calc(f, m)

            if cl and cr:
                self.F[i] = f
                return
            if not cl and not cr:
                return
            if cm:
                self.F[i], f = f, fi
                cl = not cl
            if cl:
                i *= 2
            else:
                i = i * 2 + 1


    def query(self, x):
        i = self.D[x] + self.n
        mi = self.inf
        while i > 0:
            if self.F[i]:
                mi = min(mi, self.calc(self.F[i], x))
            i >>= 1
        return mi


    def add_line(self, a, b):
        f = (a, b)
        self._update(1, f)


#########################

n, c = map(int, input().split())
h = list(map(int, input().split()))

cht = CHT(h)

cht.add_line(-2*h[0], h[0]**2)
for i in range(1, n):
    mi = cht.query(h[i])
    y = h[i]**2 + c + mi
    cht.add_line(-2*h[i], h[i]**2 + y)

print(y)
