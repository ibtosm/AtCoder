######title######
# 転倒数
######subtitle######
# inv_numbers: listを与えて反転数を出力する

##############name##############
# 転倒数
######description######
# Lib_転倒数
######body######
# 転倒数
# 配列中 i<j, ai>ajとなるものの個数
# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j
class BIT:
    def __init__(self, size):
        self.size = size; self.dat = [0]*(size+1)

    def add(self, i, x):
        i += 1
        while i <= self.size: self.dat[i] += x; i += i & -i

    def sum(self, r):
        r += 1; s = 0
        while r: s += self.dat[r];r -= r & -r
        return s

def _compress(points:list) -> list:
    sx = set(points)
    pos = {xi:i for i, xi in enumerate(sorted(set(sx)))}
    return [pos[xi] for xi in points]

def inv_numbers(a: list, compress=False) -> int:
    _a = _compress(a) if compress else a
    bit = BIT(max(_a) + 2)
    ret = 0
    for i, ai in enumerate(_a):
        ret += i - bit.sum(ai); bit.add(ai, 1)
    return ret

###################################

n = int(input())
a = list(map(int, input().split()))
ret = inv_numbers(a)
print(ret)
######prefix######
# Lib_A_転倒数
##############end##############
