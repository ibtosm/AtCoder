######title######
# SuffixArray
######subtitle######
# SuffixArray: 接尾辞を昇順に並べたもの

##############name##############
# SuffixArray
######description######
# SuffixArray
######body######
# https://atcoder.jp/contests/abc362/tasks/abc362_g

from atcoder.string import suffix_array

s = input()
sa = suffix_array(s)
n = len(s)

def bisect_left(t: str) -> int:
    # bisect_left: tが入るべき一番左
    ok = -1
    ng = n
    lt = len(t)
    while ng - ok > 1:
        mid = (ok+ng)//2
        pos = sa[mid]
        if s[pos:pos+lt] < t:
            ok = mid
        else:
            ng = mid
    return ok

def bisect_right(t: str) -> int:
    return bisect_left(t + "~")

q = int(input())
for _ in range(q):
    t = input()
    ret = bisect_right(t) - bisect_left(t)
    print(ret)

######prefix######
# Lib_Str_SuffixArray
##############end##############
