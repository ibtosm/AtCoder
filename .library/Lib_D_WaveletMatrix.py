######title######
# Wavelet Matrix
######subtitle######
# WaveletMatrix: 数列のある範囲での値の頻度やインデックスを求める
# access(k): k番目の要素の値
# select(v, k): k番目のvのインデックス
# rank(l, r, v): 区間 [l,r) に含まれる v の個数
# freq(l, r, s, t): 区間 [l,r) に含まれる要素のうち,値が[s, t) である要素の個数
# quantile(l, r, k):区間[l,r)に含まれる要素のうち,値がk番目(0-ind>k+1番目)の値
# kth_smallest(l, r, k): 区間[l,r) に含まれる要素のうち k 番目(0-indexed) に小さいものを返す.
# kth_largest(l, r, k): 区間 [l,r) に含まれる要素のうち k 番目 (0-indexed) に大きいものを返す.
# prev_value(l, r, value): 区間[l, r) に含まれる要素のうち valueより小さいもの
# next_value(l, r, value): 区間[l, r) に含まれる要素のうち value以上の値(valueのこともあり得る)

##############name##############
# Wavelet Matrix
######description######
# WaveletMatrix: 数列のある範囲での値の頻度やインデックスを求める
######body######

class WaveletMatrix:
    """
    https://judge.yosupo.jp/problem/range_kth_smallest
    https://scrapbox.io/koki/Wavelet_Matrix
    長さnの数列 a
    access(k): k番目の要素の値
    select(v, k): k番目のvのインデックス
    rank(l, r, v): 区間 [l,r) に含まれる v の個数
    freq(l, r, s, t): 区間 [l,r) に含まれる要素のうち,値が[s, t) である要素の個数
    quantile(l, r, k):区間[l,r)に含まれる要素のうち,値がk番目(0-ind>k+1番目)の値
    kth_smallest(l, r, k): 区間[l,r) に含まれる要素のうち k 番目(0-indexed) に小さいものを返す.
    kth_largest(l, r, k): 区間 [l,r) に含まれる要素のうち k 番目 (0-indexed) に大きいものを返す.
    prev_value(l, r, value): 区間[l, r) に含まれる要素のうち valueより小さいもの
    next_value(l, r, value): 区間[l, r) に含まれる要素のうち value以上の値(valueのこともあり得る)
    """
    class BitVector:
        def __init__(self, a:list):
            self.n = len(a)
            ra = [0]
            for ai in a:
                ra.append(ra[-1] + ai)
            self.ra = ra    # 累積和
        def rank0(self, r:int) -> int:
            return r - self.rank1(r)
        def rank1(self, r:int) -> int:
            return self.ra[r]

        def _bisect(l, r, isok):
            while r - l > 1:
                m = (l + r) >> 1
                if isok(m): l = m
                else: r = m
            return l

        def select0(self, k):
            l, r = 0, self.n + 1
            if not k < self.rank0(r-1): return -1
            return self._bisect(l, r, lambda m: m-self.ra[m] <= k)

        def select1(self, k):
            l, r = 0, self.n + 1
            if not k < self.ra[r-1]: return -1
            return self._bisect(l, r, lambda m: self.ra[m] <= k)

    def __init__(self, a, s=30):
        self.n = len(a)
        self.s = s # bit length
        self.a = a
        b = a[:]
        self.x = []
        for i in range(self.s)[::-1]:
            l, r, t = [], [], []
            for bi in b:
                if bi >> i & 1:
                    t.append(1); r.append(bi)
                else:
                    t.append(0); l.append(bi)
            vb = self.BitVector(t)
            self.x.append((vb.rank0(self.n), vb))
            b = l + r
        self.x = self.x[::-1]

    def access(self, k):
        """
        a[k]の値を取得:Number of value A[k]
        """
        return self.a[k]

    def rank(self, l, r, value):
        """
        A[l,r)のうちvalueの個数:Number of value's in A[l,r)
        """
        if l >= r: return 0
        for i in range(self.s)[::-1]:
            z, vb = self.x[i]
            if value >> i & 1:
                l, r = z + vb.rank1(l), z + vb.rank1(r)
            else:
                l, r = vb.rank0(l), vb.rank0(r)
        return r - l

    def select(self, value, k):
        """
        valueのk番目(0index>k+1個目)のインデックス: Index of k'th value in a (zero indexed)
        valueがk以下の場合は-1を返す
        """
        if self.rank(0, self.n, value) <= k: return -1
        ind = 0
        for i in range(self.s)[::-1]:
            z, vb = self.x[i]
            if value >> i & 1:
                ind = z + vb.rank1(ind)
            else:
                ind = vb.rank0(ind)
        ind += k
        for i in range(self.s):
            z, vb = self.x[i]
            if ind < z:
                ind = vb.select0(ind)
            else:
                ind = vb.select1(ind - z)
        return ind

    def freq(self, l, r, s, t):
        """
        A[l,r)にある要素のうち、値が[s, t)の範囲にあるものの個数
        Number of elements in A[l,r) whose value is in [s, t)
        """
        if s >= t: return 0
        return self.freq_to(l, r, t) - self.freq_to(l, r, s)

    def freq_to(self, l, r, value):
        """
        A[l,r)にある要素のうち、値が[0, value)の範囲にあるものの個数
        Number of elements in A[l,r) whose value is in [0, u)
        """
        if not value: return 0
        if l >= r: return 0
        ret = 0
        for i in range(self.s)[::-1]:
            z, vb = self.x[i]
            if value >> i & 1:
                ret += vb.rank0(r) - vb.rank0(l)
                l, r = z + vb.rank1(l), z + vb.rank1(r)
            else:
                l, r = vb.rank0(l), vb.rank0(r)
        return ret

    def quantile(self, l, r, k):
        """
        A[l,r)にある要素のうち、値がk番目(0-ind>k+1番目)の値
        k'th smallest in [l, r)
        """
        if k >= r - l: return -1
        ret = 0
        for i in range(self.s)[::-1]:
            z, vb = self.x[i]
            zeros = vb.rank0(r) - vb.rank0(l)
            if zeros > k:
                l, r = vb.rank0(l), vb.rank0(r)
            else:
                k -= zeros
                ret |= 1 << i
                l, r = z + vb.rank1(l), z + vb.rank1(r)
        return ret

    def kth_smallest(self, l, r, k):
        return self.quantile(l, r, k)

    def kth_largest(self, l, r, k):
        return self.quantile(l, r, self.n-1-k)

    def prev_value(self, l, r, value):
        cnt = self.freq_to(l, r, value)
        if cnt == 0: return -1
        return self.kth_smallest(l, r, cnt - 1)

    def next_value(self, l, r, value):
        cnt = self.freq_to(l, r, value)
        if cnt == r-l: return -1
        return self.kth_smallest(l, r, cnt)


#######################################
from bisect import bisect_left
class Compress:
    """一次元座標圧縮

    Parameters
    ----------
    points : list
    値のリスト [100,300,50,900,200]

    Returns
    -------
    pos : {50: 0, 100: 1, 200: 2, 300: 3, 900: 4}
    vals : {0: 50, 1: 100, 2: 200, 3: 300, 4: 900}
    list : [1, 3, 0, 4, 2]
    """
    def __init__(self, points, spacing=False, reverse=False):
        pos, vals, sx = {}, {}, set(points)
        if spacing: #スペースを作る場合
            for p in points: sx.add(p+1)
            sx.add(-1)
            sx.add(10**10)

        for i, xi in enumerate(sorted(set(sx), reverse=reverse)):
            pos[xi], vals[i] = i, xi
        self.pos, self.vals = pos, vals
        self.original_list, self.list = points, [pos[xi] for xi in points]
        self.valuesequence = sorted(self.pos.keys())

    def __contains__(self, original_value):
        return original_value in self.pos.keys()

    def index(self, original_value):
        # 元value -> 新index
        # if original_value in self.pos: return self.pos[original_value]
        # return None
        return bisect_left(self.valuesequence, original_value)

    def value(self, index):
        # 新index -> 元value
        if index in self.vals: return self.vals(index)
        return None

##########################################################################3

class WaveletMatrixCompressed(WaveletMatrix):
    def __init__(self, a, s=30):
        self.cmp = Compress(a)
        super().__init__(self.cmp.list, s)

    def access(self, k):
        cmppos = super().access(k)
        return self.cmp.vals[cmppos]

    def rank(self, l, r, value):
        cmpidx = self.cmp.index(value)
        return super().rank(l, r, cmpidx)

    def select(self, value, k):
        cmpidx = self.cmp.index(value)
        return super().select(cmpidx, k)

    def freq(self, l, r, s, t):
        cmpsidx = self.cmp.index(s)
        cmptidx = self.cmp.index(t)
        if s >= t: return 0
        return self.freq_to(l, r, t) - self.freq_to(l, r, s)

    def freq_to(self, l, r, value):
        cmpidx = self.cmp.index(value)
        if not cmpidx: return 0
        if l >= r: return 0
        ret = 0
        for i in range(self.s)[::-1]:
            z, vb = self.x[i]
            if cmpidx >> i & 1:
                ret += vb.rank0(r) - vb.rank0(l)
                l, r = z + vb.rank1(l), z + vb.rank1(r)
            else:
                l, r = vb.rank0(l), vb.rank0(r)
        return ret

    def quantile(self, l, r, k):
        if k >= r - l: return -1
        ret = 0
        for i in range(self.s)[::-1]:
            z, vb = self.x[i]
            zeros = vb.rank0(r) - vb.rank0(l)
            if zeros > k:
                l, r = vb.rank0(l), vb.rank0(r)
            else:
                k -= zeros
                ret |= 1 << i
                l, r = z + vb.rank1(l), z + vb.rank1(r)
        return self.cmp.vals[ret]

    def kth_smallest(self, l, r, k):
        return self.quantile(l, r, k)

    def kth_largest(self, l, r, k):
        return self.quantile(l, r, self.n-1-k)

    def prev_value(self, l, r, value):
        cnt = self.freq_to(l, r, value)
        if cnt == 0: return -1
        return self.kth_smallest(l, r, cnt - 1)

    def next_value(self, l, r, value):
        cnt = self.freq_to(l, r, value)
        if cnt == r-l: return -1
        return self.kth_smallest(l, r, cnt)


import sys
input = lambda: sys.stdin.readline().rstrip()

# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# wm = WaveletMatrix(a)
# wm = WaveletMatrixCompressed(a)
# for _ in range(q):
#     l, r, k = map(int, input().split())
#     print(wm.quantile(l, r, k))

n = int(input())
a = list(map(int, input().split()))
q = int(input())
wm = WaveletMatrixCompressed(a)
for _ in range(q):
    ret = 10**10
    l, r, d = map(int, input().split())
    r += 1
    v = wm.prev_value(l, r, d)
    if v != -1:
        ret = min(ret, d-v)
    v = wm.next_value(l, r, d)
    if v != -1:
        ret = min(ret, v-d)
    print(ret)

######prefix######
# Lib_D_WaveletMatrix
##############end##############
