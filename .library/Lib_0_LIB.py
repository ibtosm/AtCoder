##############name##############
# memo_lru_cache
######description######
# memo_lru_cache
######body######
from functools import lru_cache
@lru_cache(1000000)
######prefix######
# lru_cache_funct
##############end##############

##############name##############
# defaultdict_lib
######description######
# defaultdict_lib
######body######
from collections import defaultdict

######prefix######
# from clib defaultdict
##############end##############

##############name##############
# deque_lib
######description######
# deque_lib
######body######
from collections import deque

######prefix######
# from clib deque
##############end##############

##############name##############
# counter_lib
######description######
# counter_lib
######body######
from collections import Counter

######prefix######
# from clib Counter
##############end##############


##############name##############
# heapq_lib
######description######
# heapq_lib
######body######
from heapq import heappop, heappush
######prefix######
# from heapq
##############end##############

##############name##############
# atcoder_lib_fenwicktree
######description######
# ACL_fenwicktree
######body######
from atcoder.fenwicktree import FenwickTree
######prefix######
# from atcoder.fenwicktree
##############end##############

##############name##############
# atcoder_lib_DSU
######description######
# ACL_DSU
######body######
from atcoder.dsu import DSU
######prefix######
# from atcoder.dsu
##############end##############

##############name##############
# 順列・組み合わせ
######description######
# 順列・組み合わせ
######body######
from itertools import permutations, combinations, combinations_with_replacement, product
P = list(permutations(range(${1:n}), ${2:r}))   # 順列(nPr)
C = list(combinations(range(${1:n}, ${2:r})))   # 組み合わせ(nCr)
CR = list(combinations_with_replacement(range(${1:n}), ${2:r}))  # 重複も許容した組み合わせ(nHr=n+r-1Cr)
PN = list(product(range(${1:n}), repeat=${2:r})) # 重複順列(n**r)
T = [[1, 2],[3, 4, 5, 6],[7, 8, 9]]
PT = list(product(*T))

######prefix######
# from itertools
##############end##############
