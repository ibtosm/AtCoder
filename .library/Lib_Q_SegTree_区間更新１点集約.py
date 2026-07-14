######title######
# セグメント木双対：区間＜更新・加算・min＞・一点集約
######subtitle######
# 区間更新・一点集約
# 区間加算・一点集約
# 区間min・一点集約

##############name##############
# 双対セグメント木区間x一点
######description######
# 双対セグメント木区間x一点
######body######
class SegTree:  # 初期化処理
    """dual Segment Tree
    区間＜更新・加算・min・max＞・1点抽出
    Parameters
    ----------
    op: monoid
    e: 単位元
    v : 初期リスト/要素数
    Notes
    -----
    """
    def __init__(self, op, e, v):
        self._op = op
        self._e = (-1, e)

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self._time = 0
        self._d = [self._e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = (-1, v[i])
        for i in range(self._n):
            self._query(i)

    def update(self, l, r, x):
        """半開区間[l, r)の値を更新
        """
        _x = (self._time, x)
        l += self._size
        r += self._size
        while l < r:
            if r & 1:
                r -= 1; self._d[r] = self._op(self._d[r], _x)
            if l & 1:
                self._d[l] = self._op(self._d[l], _x); l += 1
            l >>= 1; r >>= 1
        self._time += 1

    def _query(self, k) -> tuple:
        k += self._size
        t = self._e
        while k > 0:
            if self._d[k]:
                t = self._op(t, self._d[k])
            k >>= 1
        return t

    def query(self, k: int) -> int:
        """a_kを取得
        """
        return self._query(k)[1]

    def __getitem__(self, i:int) -> tuple:
        return self.query(i)

    def __str__(self):
        """元のリストの値を表示"""
        return self._debug(self._d)

    def debug(self):
        strs = ["e" if x == self._e else str(x) for x in self._d] + [f"({x})" for x in range(self._n)]
        minsize = max(len(s) for s in strs[self._size:])
        result = ["|"] * (self._log + 2)
        level = 0
        next_level = 2
        for i in range(1, len(strs)):
            if i == next_level:
                level += 1
                next_level <<= 1
            if level < self._log + 1:
                width = ((minsize + 1) << (self._log - level)) - 1
            result[level] += strs[i].center(width) + "|"
        return "\n".join(result)



n, q = map(int, input().split())
INF = (1<<31) - 1

RUQ = SegTree(lambda x, y: max(x, y), INF, n)
RAQ = SegTree(lambda x, y: (max(x[0], y[0]), x[1]+y[1]), 0, n)
RMinQ = SegTree(lambda x, y: (max(x[0], y[0]), min(x[1],y[1])), INF, n)
RMaxQ = SegTree(lambda x, y: (max(x[0], y[0]), max(x[1],y[1])), INF, n)


# 1-indexed
# https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_D
# https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_E

for _ in range(q):
    t, *qry = map(int, input().split())
    if t == 0:
        l, r, x = qry
        # l -= 1
        r += 1
        RUQ.update(l, r, x)
    else:
        i = qry[0]
        # i -= 1
        print(RUQ.query(i))
    print(RUQ.debug())
######prefix######
# Lib_Q_SegDual_双対_区間更新一点集約
##############end##############
