######title######
# 削除機能付きheapque
######subtitle######
# DeletableHeapq: クラス
# DeletableMaxMinHeapQ: クラス
# heappush:
# heappopmax: 大きいものを取り出す
# heappopmin: 小さいものを取り出す
# heapmax: 大きいものにアクセス
# heapmin: 小さいものにアクセス
# discard(x): xを削除

##############name##############
# 削除機能付きHeapque
######description######
# 削除機能付きHeapque
######body######

from heapq import heapify, heappush, heappop
class Heapq:
    def __init__(self, a=None):
        self.q = a if a else []
        self.p = []
        heapify(self.q)

    def heappush(self, x):
        heappush(self.q, x)
    def discard(self, x):
        heappush(self.p, x)
    def _clean(self):
        while self.p and self.q[0]==self.p[0]:
            heappop(self.q)
            heappop(self.p)
    def pop(self, exc=None):
        self._clean()
        if self.q:
            return heappop(self.q)
        return exc
    def heapmin(self, exc=None):
        self._clean()
        if self.q:
            return self.q[0]
        return exc
######prefix######
# Lib_D_heapque_min
##############end##############


##############name##############
# 削除機能付きMaxMinheapque
######description######
# 削除機能付きMaxMinheapque
######body######
from heapq import heappush, heappop
from collections import defaultdict
class DeletableMaxMinHeapq():
    def __init__(self):
        self.Hma = []
        self.Hmi = []
        self.HC = defaultdict(int)
    def heappush(self, x):
        heappush(self.Hma, -x)
        heappush(self.Hmi, x)
        self.HC[x] += 1
    def heappopmax(self):
        t = -heappop(self.Hma)
        while not self.HC[t]:
            t = -heappop(self.Hma)
        self.HC[t] -= 1
        return t
    def heappopmin(self):
        t = heappop(self.Hmi)
        while not self.HC[t]:
            t = heappop(self.Hmi)
        self.HC[t] -= 1
        return t
    def heapmax(self):
        t = -self.Hma[0]
        while not self.HC[t]:
            heappop(self.Hma)
            t = -self.Hma[0]
        return t
    def heapmin(self):
        t = self.Hmi[0]
        while not self.HC[t]:
            heappop(self.Hmi)
            t = self.Hmi[0]
        return t
    def dicard(self, x):
        assert self.HC[x] > 0
        self.HC[x] -= 1
    def __contains__(self, x):
        return 1 if x in self.HC and self.HC[x] else 0

hq = DeletableMaxMinHeapq()
n, q = map(int, input().split())
a = list(map(int, input().split()))
for ai in a:
    hq.heappush(ai)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        hq.heappush(query[1])
    elif query[0] == 1:
        x = hq.heappopmin()
        print(x)
    else:
        x = hq.heappopmax()
        print(x)


# https://judge.yosupo.jp/problem/double_ended_priority_queue

############

######prefix######
# Lib_D_heapque_minmax
##############end##############
