######title######
# 遅延評価セグメント木
######subtitle######
# 遅延評価セグメント木
# op: モノイド演算 | e: 単位元
# mapping: 作用
# composition: 作用の合成
# id: 恒等作用
# v: サイズまたは初期配列

##############name##############
# 遅延評価セグメント木
######description######
# 遅延評価セグメント木

######body######


# https://github.com/ibtosm/AtCoder/blob/main/.library/RM_LazySegTree.md

# LazySegTree:(op, e, mapping, composition, id_, v)
# op: モノイド演算, e: 単位元,
# mapping: 作用素| composition: 作用素の合成 | id_: 作用素の単位元
# v: サイズまたは初期配列
# set(p, x)            # 1点更新
# get(p)               # 1点取得
# prod(l, r)           # 区間集約
# all_prod()           # 全体集約
# apply(p, f)          # 1点作用
# apply(l, r, f)       # 区間作用
# max_right(l, isOk)   # セグ木上二分探索
# min_left(r, isOk)    # セグ木上二分探索

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
    from cpdebug.lazysegtree import (
        dump,
        dump_max_right,
        dump_min_left,
        dump_raw,
        dump_values,
    )

from atcoder.lazysegtree import LazySegTree


def op(a, b):
    return a + b


e = 0


def mapping(f, x):
    return x + f


def composition(f, g):
    return f + g


id_ = 0

A = [1, 2, 3, 4, 5, 6, 7, 8]

lst = LazySegTree(
    op,
    e,
    mapping,
    composition,
    id_,
    A,
)

dump(lst)
dump_raw(lst)
dump_values(lst)


######prefix######
# Lib_Q_LazySegTree
##############end##############
