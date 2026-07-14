######title######
# ローリングハッシュ
######subtitle######
# RollingHash: 文字列が一致しているか判定する

##############name##############
# ローリングハッシュ
######description######
######body######
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bd

from random import randint
mod1 = 2**61 - 1
mod2 = 1000000007
base1 = randint(1,mod1-1)
base2 = randint(1,mod2-1)

class RollingHash:
    mod1 = mod1
    mod2 = mod2
    base1 = base1
    base2 = base2
    def __init__(self, S:str) -> None:
        self.S = S
        self.size = len(S)
        self.hash1 = [0] * (n + 1)
        self.hash2 = [0] * (n + 1)
        self.power1 = [1] * (n + 1)
        self.power2 = [1] * (n + 1)

        for i in range(self.size):
            self.hash1[i+1] = (self.hash1[i] * self.base1 + ord(S[i])) % self.mod1
            self.hash2[i+1] = (self.hash2[i] * self.base2 + ord(S[i])) % self.mod2
            self.power1[i+1] = (self.power1[i] * self.base1) % self.mod1
            self.power2[i+1] = (self.power2[i] * self.base2) % self.mod2

    def get(self, l:int, r:int) -> tuple:
        """部分文字列 S[l:r] のハッシュ取得"""
        res1 = (self.hash1[r] - self.hash1[l] * self.power1[r - l]) % self.mod1
        res2 = (self.hash2[r] - self.hash2[l] * self.power2[r - l]) % self.mod2
        return (res1, res2)

    def getLCP(self, a:int, b:int) -> int:
        """S[a:] と S[b:] の最長共通接頭辞の長さ"""
        len_ = min(self.size - a, self.size - b)
        low, high = 0, len_
        while high - low > 1:
            mid = (low + high) // 2
            if self.get(a, a + mid) != self.get(b, b + mid):
                high = mid
            else:
                low = mid
        return low

    def getLCP_with(self, a:int, other_hash, b:int):
        """自身の文字列 S[a:] と、別の文字列 T[b:] の最長共通接頭辞の長さ"""
        len_ = min(self.size - a, other_hash.size - b)
        low, high = 0, len_
        while high - low > 1:
            mid = (low + high) // 2
            if self.get(a, a + mid) != other_hash.get(b, b + mid):
                high = mid
            else:
                low = mid
        return low


n, q = map(int, input().split())
s = input()
RHS = RollingHash(s)

for _ in range(q):
    a, b, c, d = map(int, input().split())
    a -= 1; c -= 1
    hash1 = RHS.get(a, b)
    hash2 = RHS.get(c, d)

    if hash1 == hash2:
        print('Yes')
    else:
        print('No')

######prefix######
# Lib_Str_RollingHash
##############end##############

##############name##############
# 動的ローリングハッシュ(１点更新)
######description######
######body######
# https://atcoder.jp/contests/abc331/tasks/abc331_f

from atcoder.segtree import SegTree
from random import randint
n = 10**6
mod = 2**61 - 1
base = randint(1,mod-1)
pw = [1]
for _ in range(n):
    pw.append(pw[-1]*base%mod)


def op(x, y):
    # xh: ハッシュ値, xl: 区間の長さ
    xh, xl = x
    yh, yl = y
    nh = (xh * pw[yl] % mod + yh) % mod
    nl = xl + yl
    return (nh, nl)


class RollingHashSegTree:
    def __init__(self, S: str) -> None:
        self.sgt = SegTree(op, (0,0), [(ord(c), 1) for c in S])
        self.size = len(S)

    def update(self, i: int, c: str) -> None:
        self.sgt.set(i, (ord(c), 1))

    def get(self, l: int, r:int) -> int:
        return self.sgt.prod(l, r)

    def getLCP(self, a:int, b:int) -> int:
        """S[a:] と S[b:] の最長共通接頭辞の長さ"""
        len_ = min(self.size - a, self.size - b)
        low, high = 0, len_
        while high - low > 1:
            mid = (low + high) // 2
            if self.get(a, a + mid) != self.get(b, b + mid):
                high = mid
            else:
                low = mid
        return low

    def getLCP_with(self, a:int, other_hash, b:int):
        """自身の文字列 S[a:] と、別の文字列 T[b:] の最長共通接頭辞の長さ"""
        len_ = min(self.size - a, other_hash.size - b)
        low, high = 0, len_
        while high - low > 1:
            mid = (low + high) // 2
            if self.get(a, a + mid) != other_hash.get(b, b + mid):
                high = mid
            else:
                low = mid
        return low


n, q = map(int, input().split())
s = input()
left = RollingHashSegTree(s)
right = RollingHashSegTree(s[::-1])

for _ in range(q):
    query = list(input().split())
    if query[0] == "1":
        x, c = query[1:]
        x = int(x) - 1
        left.update(x, c)
        right.update(n-1-x, c)
    else:
        l, r = map(int, query[1:])
        print('Yes' if left.get(l-1, r) == right.get(n-r, n-l+1) else 'No')

######prefix######
# Lib_Str_RollingHash
##############end##############
