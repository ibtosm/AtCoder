##############name##############
# reverse=True
######description######
# ソートでのリバース
######body######
reverse=True
######prefix######
# reverse=True
##############end##############

##############name##############
# sort(key=itemgetter
######description######
# itemgetterソート
######body######
sort(key=lambda x: x[1])
######prefix######
# sort(key=l
##############end##############

##############name##############
# 順列・組み合わせ
######description######
# 順列・組み合わせ
######body######
from itertools import permutations, combinations, combinations_with_replacement, product
P = list(permutations(range($n), r))   # 順列(nPr)
C = list(combinations(range($n), r))   # 組み合わせ(nCr)
CR = list(combinations_with_replacement(range($n), r))  # 重複も許容した組み合わせ(nHr=n+r-1Cr)
PN = list(product(range($n), repeat=r)) # 重複順列(n**r)
T = [[1, 2],[3, 4, 5, 6],[7, 8, 9]]
PT = list(product(*T))


######prefix######
# itertools
# Lib_順列・組み合わせ
##############end##############

##############name##############
# directions_RULD
######description######
# directions_RULD
######body######

directions_str = {"R":(1, 0), "U":(0, 1), "L":(-1, 0), "D":(0, -1)}

######prefix######
# directions_RULD
##############end##############

##############name##############
# directions4
######description######
# directions4
######body######
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def move(cur:tuple, d:tuple) -> None|tuple:
    next0 = cur[0] + d[0]
    next1 = cur[1] + d[1]

    if (0 <= next0 < H) and (0 <= next1 < W):
        return (next0, next1)
    return (None, None)

######prefix######
# directions4
##############end##############



##############name##############
# directions8
######description######
# directions8
######body######
directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def move(cur:tuple, d:tuple) -> None|tuple:
    next0 = cur[0] + d[0]
    next1 = cur[1] + d[1]

    if (0 <= next0 < H) and (0 <= next1 < W):
        return (next0, next1)
    return None

######prefix######
# directions8
##############end##############
