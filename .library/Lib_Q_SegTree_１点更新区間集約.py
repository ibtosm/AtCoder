######title######
# セグメント木１点更新区間集約
######subtitle######
# op: モノイドの演算 | e: モノイドの単位元 | v: 要素数orリスト
##############name##############
# セグメント木１点更新区間集約
######description######
# セグメント木１点更新区間集約
######body######

# https://github.com/ibtosm/AtCoder/blob/main/.library/RM_SegTree.md
# SegmentTree(op, e, v):
# op: モノイド演算, e: 単位元, v: サイズまたは初期配列

# max_right(l, isOk)
# 区間 [l, r) の集約値 x が isOk(x) を満たす最大の r
#
# - r = l      : a[l] を含めた時点で NG になる
# - l < r < n  : [l, r) は OK, [l, r] は NG
# - r = n      : [l, n) を最後まで伸ばしても OK
#
# min_left(r, isOk)
# 区間 [l, r) の集約値 x が isOk(x) を満たす最小の l
#
# - l = r      : a[r-1] を含めた時点で NG になる
# - 0 < l < r  : [l, r) は OK, [l-1, r) は NG
# - l = 0      : [0, r) を最後まで伸ばしても OK
#
# 前提:
#   isOk(e) == True
#   isOk は単調

DEBUG = True

if DEBUG:
    import sys

    sys.path.extend([r".library", r"../../.library"])
    from cpdebug.segtree import dump, dump_max_right, dump_min_left

from atcoder.segtree import SegTree

A = [1, 2, 3, 4, 5, 6, 7, 8]

sgt = SegTree(lambda a, b: a + b, 0, A)

f = lambda x: x < 12

dump(sgt)
dump(sgt, 2, 7)
dump_max_right(sgt, 2, f)
dump_min_left(sgt, 7, f)


######prefix######
# Lib_Q_Seg_一点更新区間集約
##############end##############
