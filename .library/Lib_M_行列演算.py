######title######
# 行列演算
######subtitle######
# prod: (ma*mb, mod)行列の掛け算(modで)
# powmat: 正方行列のべき乗計算
# trans: 転置行列を返す
# rotate: 90度回転 reverse = True時計 False反時計
# gauss_jordan: F2(二進数)での上三角行列
# solve_linear_equation: F2(二進数)でAx=bとなるxを求める

##############name##############
# 行列演算
#descripiton#
# 行列演算
######body######

def matprod(ma, mb, mod = 10**9+7):
    h_a = len(ma)   # n
    w_a = len(ma[0])    # m
    h_b = len(mb)   # m
    w_b = len(mb[0])    # k
    assert(w_a == h_b)
    assert(h_a*w_a*h_b*w_b)

    tmb = [list(x) for x in zip(*mb)]
    ret = [[0] * w_b for _ in range(h_a)]
    for _i, mai in enumerate(ma):
        reti = ret[_i]
        for _j, mbk in enumerate(tmb):
            reti[_j] = sum(a*b%mod for a, b in zip(mai, mbk)) % mod
    return ret


def matpow(ma, k, mod = 10**9+7):
    n = len(ma)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        ret[i][i] = 1
    for _ in range(k):
        if k & 1:
            ret = matprod(ret, ma, mod)
        ma = matprod(ma, ma, mod)
        k >>= 1
        if k == 0: break
    return ret

mod = 998244353
n, m, k = map(int, input().split())
ma = [list(map(int, input().split())) for _ in range(n)]
mb = [list(map(int, input().split())) for _ in range(m)]



for r in matprod(ma, mb, mod):
    print(*r)


######prefix######
# Lib_M_行列演算_matrix
##############end##############


##############name##############
# 転置行列
######description######
# 転置行列
######body######
def trans(A):
    return [list(x) for x in zip(*A)]
######prefix######
# transpose_matrix
##############end##############


##############name##############
# 行列90度回転
######description######
# 行列90度回転
######body######
def rotate(A, reverse = False):
    if reverse:
        return [list(x) for x in zip(*A)][::-1]
    else:
        return [list(x) for x in zip(*A[::-1])]
######prefix######
# Lib_M_rotate_matrix
##############end##############


##############name##############
# F2(2進数)での上三角行列生成
######description######
# F2(2進数)での上三角行列生成
######body######
def gauss_jordan(ma):
    n, m = len(ma), len(ma[0])
    rank = 0
    for col in range(m):
        if rank>=n: break
        if ma[rank][col] == 0:
            for row in range(rank+1, n):
                if ma[row][col]:
                    ma[rank], ma[row] = ma[row], ma[rank]
                    break
        if ma[rank][col] == 1:
            for row in range(rank+1, n):
                if ma[row][col]:
                    for _col in range(col, m):
                        ma[row][_col] ^= ma[rank][_col]
            rank += 1
    return ma, rank

######prefix######
# Lib_M_上三角行列
##############end##############

##############name##############
# F2(2進数)でのA・x = b となるxを見つける
######description######
# F2(2進数)でのA・x = b となるxを見つける
######body######
def solve_linear_equation(A, b):
    """A・x = b となるxを見つける"""
    h, w = len(A), len(A[0])
    """extend"""
    _A = []
    for Ai, bi in zip(A, b):
        _A.append(Ai + [bi])
    rank = 0
    for col in range(w):
        for row in range(rank, h):
            if _A[row][col]:
                _A[row], _A[rank] = _A[rank], _A[row]
                break
        else: continue
        for row in range(h):
            if row != rank and _A[row][col]:
                for _col in range(w + 1):
                    _A[row][_col] ^= _A[rank][_col]
        rank += 1
    # for ai in A: print(ai)
    # print("---")
    # for ai in _A: print(ai)
    # print(rank)
    return _A, rank

######prefix######
# Lib_M_線形方程式
##############end##############

# class MatrixMod:
#     def __init__(self, n: int, m: int, from_array= None) -> None:
#         self._n = n
#         self._m = m
#         if from_array is None:
#             self._matrix = [[0] * m for _ in range(n)]
#         else:
#             self._matrix = [row[:] for row in from_array]

#     @classmethod
#     def ie(cls, n: int) -> "MatrixMod":
#         ret = cls(n, n)
#         for i in range(n):
#             ret[i, i] = 1
#         return ret

#     def is_square(self) -> bool:
#         return self._n == self._m

#     def __str__(self) -> str:
#         return "\n".join(" ".join(map(str, row)) for row in self._matrix)

#     def __getitem__(self, idxs) -> int:
#         return self._matrix[idxs[0]][idxs[1]]

#     def __setitem__(self, idxs, value: int) -> None:
#         self._matrix[idxs[0]][idxs[1]] = value

#     def __add__(self, other: 'MatrixMod') -> 'MatrixMod':
#         assert self._n == other._n and self._m == other._m
#         ret = MatrixMod(self._n, self._m)
#         for i in range(self._n):
#             res_i = ret._matrix[i]
#             self_i = self._matrix[i]
#             other_i = other._matrix[i]
#             for j in range(self._m):
#                 res_i[j] = (self_i[j] + other_i[j]) % MOD
#         return ret

#     def __pos__(self) -> 'MatrixMod':
#         return self

#     def __neg__(self) -> 'MatrixMod':
#         ret = MatrixMod(self._n, self._m)
#         for i in range(self._n):
#             res_i = ret._matrix[i]
#             self_i = self._matrix[i]
#             for j in range(self._m):
#                 res_i[j] = -self_i[j] % MOD
#         return ret

#     def __sub__(self, other: 'MatrixMod') -> 'MatrixMod':
#         assert self._n == other._n and self._m == other._m
#         ret = MatrixMod(self._n, self._m)
#         for i in range(self._n):
#             res_i = ret._matrix[i]
#             self_i = self._matrix[i]
#             other_i = other._matrix[i]
#             for j in range(self._m):
#                 res_i[j] = (self_i[j] - other_i[j]) % MOD
#         return ret

#     def __mul__(self, other: 'MatrixMod') -> 'MatrixMod':
#         assert self._m == other._n
#         ret = MatrixMod(self._n, other._m)
#         for i in range(self._n):
#             res_i = ret._matrix[i]
#             self_i = self._matrix[i]
#             for k in range(self._m):
#                 self_ik = self_i[k]
#                 other_k = other._matrix[k]
#                 for j in range(other._m):
#                     res_i[j] += self_ik * other_k[j]
#                     res_i[j] %= MOD
#         return ret

#     def times(self, k: int) -> 'MarixMod':
#         ret = MatrixMod(self._n, self._m)
#         for i in range(self._n):
#             res_i = ret._matrix[i]
#             self_i = self._matrix[i]
#             for j in range(self._m):
#                 res_i[j] = self_i[j] * k % MOD
#         return ret

#     def __pow__(self, k: int) -> 'MatrixMod':
#         assert self._n == self._m
#         ret = MatrixMod.ie(self._n)
#         tmp = self
#         while k:
#             if k & 1:
#                 ret = ret * tmp
#             tmp = tmp * tmp
#             k >>= 1
#         return ret
