######title######
# ランレングス圧縮
######subtitle######
# 文字列を文字＋個数で表記する

##############name##############
# ランレングス圧縮
######description######
# ランレングス圧縮
######body######
#####################################
from itertools import groupby
strings = "aabbbbbbbbbbbba"
strings = [1,3,4,1,1,1,5,5,7]

rle = [(k, len(list(g))) for k,g in groupby(strings)]
split = [list(g) for k, g in groupby(strings)]
print(rle)
print(split)
#[('a', 2), ('b', 12), ('a', 1)]
######prefix######
# Lib_A_ランレングス圧縮_rle
##############end##############
