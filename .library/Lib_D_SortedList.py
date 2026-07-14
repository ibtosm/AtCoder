######title######
# 順序付きリスト
######subtitle######
# SortedList:クラス

##############name##############
# Sorted List
######description######
######body######

from sortedcontainers import SortedList as SL


class SortedList(SL):
    def __init__(self, iterable=None, key=None):
        super().__init__(iterable, key)

    def lt(self, value):
        "Find the largest element < x, or None if it doesn't exist."
        if self[0] < value:
            return self[self.bisect_left(value) - 1]
        return None

    def le(self, value):
        "Find the largest element <= x, or None if it doesn't exist."
        if self[0] <= value:
            return self[self.bisect_right(value) - 1]
        return None

    def gt(self, value):
        "Find the smallest element > x, or None if it doesn't exist."
        if self[-1] > value:
            return self[self.bisect_right(value)]
        return None

    def ge(self, value):
        "Find the smallest element >= x, or None if it doesn't exist."
        if self[-1] >= value:
            return self[self.bisect_left(value)]
        return None


######prefix######
# Lib_D_sorted_list
##############end##############
