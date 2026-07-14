##############name##############
# 半分全列挙
######description######
# 半分全列挙
######body######
# https://atcoder.jp/contests/abc184/tasks/abc184_f
# 半分全列挙
# n <= 40 だと半分で全列挙したものをそれぞれ計算してマージ処理する

n, t = map(int, input().split())
vs = list(map(int, input().split()))

def get_list(vl):
    ret = [0]
    svl = sorted(vl)
    for vi in svl:
        for j in range(len(ret)):
            x = vi + ret[j]
            if x > t: continue
            ret.append(x)
    return sorted(ret)

lower = get_list(vs[:n//2])
upper = get_list(vs[n//2:])

ret = 0
up = len(upper) - 1
for f in lower:
    while up >= 0 and (upper[up]+f) > t:
        up -= 1
    ret = max(ret, upper[up]+f)

print(ret)

######prefix######
# Lib_A_半分全列挙
##############end##############
