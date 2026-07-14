######title######
# FloorSum（二次平面の線の下にある整数点の個数）
######subtitle######
# FloorSum（一次直線の下にある整数点の個数）
# その他 https://kanpurin.hatenablog.com/entry/2021/12/07/211249

##############name##############
# フロアサム
#descripiton#
# 一次直線(y=ax+b (0<=x<n の下にあるmの倍数の整数点の個数)
######body######

from atcoder.math import floor_sum

for _ in range(int(input())):
    n, m, a, b = map(int, input().split())
    print(floor_sum(n, m, a, b))

######prefix######
# Lib_N_floor_sum
##############end##############
