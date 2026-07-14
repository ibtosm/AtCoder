######title######
# ユークリッド互除法

######subtitle######
# gcd(x, y): xとyの最大公約数を求める
# extgcd(x, y): ax + by = d ,  d = gcd(x, y)となるa, b, dを出力

##############name##############
# ユークリッド互除法
#descripiton#
# gcd, extgcd
######body######

INF = 1 << 64
import math

# math.gcd(a, b)
# math.lcm(a, b)

def extgcd(a, b):
    """
    d = gcd(a, b)
    ax + by = d となるx, y, dを出力
    """
    if b == 0:
        return (1, 0, a)
    q, r = a // b, a % b
    x, y, d = extgcd(b, r)
    s, t = y, x - q * y
    return s, t, d


######prefix######
# Lib_N_gcd_ユークリッド互除法
##############end##############
