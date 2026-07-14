######title######
# 遅延評価セグメント木plain
######subtitle######
# 遅延評価セグメント木plain
# LazySegTree:(op, e, mapping, composition, id_, v)

##############name##############
# 遅延評価セグメント木plain
######description######
# 遅延評価セグメント木

######body######
from atcoder.lazysegtree import LazySegTree as LazySegTreeACL


class LazySegTree(LazySegTreeACL):
    def __init__(self, op, e, mapping, composition, id_, v):
        super().__init__(op, e, mapping, composition, id_, v)

    def __str__(self) -> str:
        return " ".join(map(str, [self.get(i) for i in range(self._n)]))

    def debug(self, xs):
        strs = [str(x) for x in xs] + [f"({x})" for x in range(self._n)]
        minsize = max(len(s) for s in strs[self._size :])
        result = ["|"] * (self._log + 2)
        level = 0
        next_level = 2
        width = 0
        for i in range(1, len(strs)):
            if i == next_level:
                level += 1
                next_level <<= 1
            if level < self._log + 1:
                width = ((minsize + 1) << (self._log - level)) - 1
            result[level] += strs[i].center(width) + "|"
        return "\n".join(result)

    # https://github.com/atcoder/ac-library/blob/master/document_ja/lazysegtree.md
    # set(p, x): p番目の要素をxに置き換える
    # get(p, x): p番目の要素を取得する
    # prod(l, r): 半開区間[l, r)の計算結果を取得する
    # all_prod(): 全区間[0, self._n)計算結果を取得する
    # apply(l, r, f): 半開区間[l, r)の各要素にfを施す
    # max_right(l, isok): g(v[i])がTrueとなる一番右のindex（lからスタート）
    # min_left(r, isok): g(v[i])がTrueとなる一番左のindex（rからスタート）


#######################################################

# INF = 10 ** 18
# RMinQ and RAQ
# LST = LazySegmentTree(min, INF, lambda f, x: f+x, lambda f, g: f+g, 0, [0]*N)
# RMaxQ and RAQ
# LST = LazySegmentTree(max, -INF, lambda f, x: f+x, lambda f, g: f+g, 0, [0]*N)
# #RSumQ and RAQ
# op = lambda x, y: (x[0]+y[0], x[1]+y[1])
# mp = lambda f, x: (x[0]+f*x[1], x[1])
# LST = LazySegmentTree(op, (0,0), mp, lambda f, g: f+g, 0, [(0,1)]*N)
# #RMinQ and RUQ
# LST = LazySegmentTree(min, INF, lambda f, x: x if f == INF else f, lambda f, g: g if f == INF else f, INF, [INF]*N)
# #RMaxQ and RUQ
# LST = LazySegmentTree(max, -INF, lambda f, x: x if f == -INF else f, lambda f, g: g if f == -INF else f, -INF, [-INF]*N)
# #RSumQ and RUQ
# op = lambda x, y: (x[0]+y[0], x[1]+y[1])
# mp = lambda f, x: x if f == INF else (f*x[1], x[1])
# LST = LazySegmentTree(op, (0,0), mp, lambda f, g: g if f == INF else f, INF, [(0,1)]*N)


# https://github.com/ibtosmlin/atcoder/blob/main/lib/lib/Memo_%E9%81%85%E5%BB%B6%E8%A9%95%E4%BE%A1Seg%E6%9C%A8.md
#######################################################
# 区間集約演算 *: G * G -> G の定義.
def op(x, y):
    invx, c0x, c1x = x
    invy, c0y, c1y = y
    return (invx + invy + c0y * c1x, c0x + c0y, c1x + c1y)


# op演算の単位元(反転数,区間内の０の数,区間内の１の数)
e = (0, 0, 0)


# 区間更新演算 ·: F · G -> G の定義.
def mapping(f, x):
    if f == 0:
        return x
    inv, c0, c1 = x
    return (c1 * c0 - inv, c1, c0)


# 遅延評価演算 ·: F · F -> F の定義.
def composition(f, g):
    return f ^ g


# 遅延評価演算の単位元
id = 0

n, q = map(int, input().split())
a = []
for i in map(int, input().split()):
    if i == 1:
        a.append((0, 0, 1))
    else:
        a.append((0, 1, 0))
sgt = LazySegTree(op, e, mapping, composition, id, a)


######prefix######
# Lib_Q_LazySeg_plain
##############end##############
