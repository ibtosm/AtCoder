##############name##############
# BITset
######description######
# BITset
######body######

def popcount64(n):
    c=(n&0x5555555555555555)+((n>>1)&0x5555555555555555)
    c=(c&0x3333333333333333)+((c>>2)&0x3333333333333333)
    c=(c&0x0f0f0f0f0f0f0f0f)+((c>>4)&0x0f0f0f0f0f0f0f0f)
    c=(c&0x00ff00ff00ff00ff)+((c>>8)&0x00ff00ff00ff00ff)
    c=(c&0x0000ffff0000ffff)+((c>>16)&0x0000ffff0000ffff)
    c=(c&0x00000000ffffffff)+((c>>32)&0x00000000ffffffff)
    return c

def bitset(s, b, m):
    """
        sをbビットずつ下からm個に区切る
    """
    s = list(map(int, s))
    ret = [0] * m
    s = [0] * (b*m - len(s)) + s
    for i in range(m):
        bit = 0
        for j in range(b):
            bit |= s[i * b + j] << j
        ret[i] = bit
    return ret

# https://atcoder.jp/contests/abc258/tasks/abc258_g

######prefix######
# Lib_BITSET
##############end##############
