######title######
# セグメント木１点更新区間集約
######subtitle######
# SegmentTree(op, e, v):
# op: モノイドの演算
# e: モノイドの単位元
# v: 要素数orリスト

##############name##############
# セグメント木１点更新区間集約
######description######
# セグメント木１点更新区間集約
######body######

from atcoder.segtree import SegTree


def debug(sgt, ql, qr, op_name="op"):
    print("-" * 30)
    seg = [None] * (2 * sgt._size)

    def dfs(k, l, r):
        seg[k] = l, r
        if k < sgt._size:
            m = (l + r) // 2
            dfs(k * 2, l, m)
            dfs(k * 2 + 1, m, r)

    dfs(1, 0, sgt._size)

    l, r = ql + sgt._size, qr + sgt._size
    left, right = [], []

    while l < r:
        if l & 1:
            left.append(l)
            l += 1
        if r & 1:
            r -= 1
            right.append(r)
        l >>= 1
        r >>= 1

    nodes = left + right[::-1]  # 非可換対応
    vals = [sgt._d[k] for k in nodes]

    print(f"[{ql},{qr})")

    for i, k in enumerate(nodes):
        L, R = seg[k]
        print(f"{'└─' if i + 1 == len(nodes) else '├─'} #{k} [{L},{R}) = {sgt._d[k]}")

    print(f"\n{op_name}({', '.join(map(str, vals))})")
    print("=", sgt.prod(ql, qr))
    print("-" * 30)

####################################

# https://atcoder.jp/contests/practice2/tasks/practice2_j
N, Q = map(int, input().split())
A = list(map(int, input().split()))
op = max; e = -10**18 #or 0
sgt = SegTree(op, e, A)
for _ in range(Q):
    t, u, v = map(int, input().split())
    if t == 1:
        sgt.set(u-1, v)
    elif t == 2:
        print(sgt.prod(u-1, v))
    else:
        print(sgt.max_right(u-1, lambda y: y<v) + 1)


# def max_right(self, l, isOk):
    # ex:
    # maxの場合 a[l]  a[r-1] が isOKとなる最大の値
    # (1): 関数 bool isOk(x) を定義し、segtreeの上で二分探索をする。
    # (2): 木の値を引数にとりboolを返す関数オブジェクトを渡して使用します。
    # r = l もしくは f(op(a[l], a[l + 1], ..., a[r - 1])) = true
    # r = n もしくは f(op(a[l], a[l + 1], ..., a[r])) = false
    # fが単調だとすれば、f(op(a[l], a[l + 1], ..., a[r - 1])) = true となる最大のr

# def min_left(self, r, isOk):
#     l = r もしくは f(op(a[l], a[l + 1], ..., a[r - 1])) = true
#     l = 0 もしくは f(op(a[l-1], a[l], ..., a[r-1])) = false
#     fが単調だとすれば、f(op(a[l], a[l + 1], ..., a[r - 1])) = true となる最小のl


######prefix######
# Lib_Q_Seg_一点更新区間集約
##############end##############
