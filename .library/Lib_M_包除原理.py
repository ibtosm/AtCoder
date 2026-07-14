##############name##############
# 包除原理
######subtitle######
# n(A or B or C) = n(A) + n(B) + n(C)
#                  -n(A&B) -n(B&C) -n(C&A)
#                  +n(A&B&C)

######description######
# 包除原理
######body######

n, d = map(int, input().split())
a = list(map(int, input().split()))

def cnt(b):
    cntzero = d - bin(b).count('1')
    return 1 << cntzero

ret = 0
# bit全探索
for i in range(1, 1<<n):
    num = 0
    c = 0
    for j in range(n):
        if i>>j & 1:
        # iで考える集合jが存在する場合
            num |= a[j]
            c += 1
    #x = n(****)
    x = cnt(num)
    #次数によりプラスとマイナスを変える
    if c%2 == 1:
        ret += x
    else:
        ret -= x

ret = (1 << d) - ret

print(ret)

######prefix######
# Lib_M_包除原理_houjo
##############end##############
