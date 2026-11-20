######title######
# 順序付き集合/リスト
######subtitle######
# SortedSet_SortedList:クラス

##############name##############
# Sorted Set/List
######description######
# SortedList を使った前後探索ユーティリティ。
# 各関数は O(log N)。該当する要素がなければ None を返す。
#
######body######

from sortedcontainers import SortedList, SortedSet


def get_lt(sl:"SortedList", x):
    "Find the largest element < x, or None if it doesn't exist."
    if not sl or x <= sl[0]:
        return None
    return sl[sl.bisect_left(x) - 1]


def get_le(sl:"SortedList", x):
    "Find the largest element <= x, or None if it doesn't exist."
    if not sl or x < sl[0]:
        return None
    return sl[sl.bisect_right(x) - 1]


def get_gt(sl:"SortedList", x):
    "Find the smallest element > x, or None if it doesn't exist."
    if not sl or sl[-1] <= x:
        return None
    return sl[sl.bisect_right(x)]


def get_ge(sl:"SortedList", x):
    "Find the smallest element >= x, or None if it doesn't exist."
    if not sl or sl[-1] < x:
        return None
    return sl[sl.bisect_left(x)]


######prefix######
# Lib_D_sorted_set_list
##############end##############
