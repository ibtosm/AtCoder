######title######
# 順列のライブラリ
######subtitle######
# permutationクラス:
# id_of_permutation(): 何番目か
# kth_permutation(k): k番目を出力
# prev():前の順列
# next():次の順列

##############name##############
# Lib_permutation
######description######
# 順列のライブラリ
######body######

from typing import Any


class Permutation:
    def __init__(self, L: list[Any]) -> None:
        self.n: int = len(L)
        self.L: list[Any] = L
        self.LS: list[Any] = sorted(L[:])
        self.map: dict[Any, int] = {li: i for i, li in enumerate(iterable=self.LS)}
        nn: int = self.n + 1
        fa: list[int] = [1] * (nn + 1)
        for i in range(nn):
            fa[i + 1] = fa[i] * (i + 1)
        self.fa: list[int] = fa
        self.convL: list[int] = self._convL(self.L)
        self.facn: int = self.fa[self.n]
        self.k: int = self.id_of_permutation(self.L)

    def _convL(self, L: list[Any]) -> list[int]:
        return [self.map[li] for li in L]

    def _restoreP(self, P: list[int]):
        return [self.LS[i] for i in P]

    def _kth_permutation(self, k: int) -> list[Any]:
        # zero-indexed here
        n: int = self.n
        S: list[int] = [i for i in range(n)]
        L: list[Any] = []
        for i in range(n):
            a: int = self.fa[n - 1 - i]
            j: int = k // a
            k %= a
            L.append(S[j])
            S: list[int] = S[:j] + S[j + 1 :]
        return L

    def _id_of_permutation(self, P: list[int]) -> int:
        # zero-indexed here
        ret = 0
        while len(P) > 1:
            a: int = len([i for i in P if i < P[0]])
            ret += a * self.fa[len(P) - 1]
            P: list[int] = P[1:]
        return ret

    def id_of_permutation(self, L=None) -> int:
        """
        return: 順列の辞書順
        """
        if L:
            P: list[int] = self._convL(L)
            return self._id_of_permutation(P)
        else:
            return self.k

    def kth_permutation(self, k) -> list:
        """
        return: k番目の順列
        """
        P: list[Any] = self._kth_permutation(k)
        return self._restoreP(P)

    def previous_item(self, L=None) -> Any:
        """
        return: 初期順列または入力順列のひとつ前
        """
        if L:
            k: int = self.id_of_permutation(L)
        else:
            k: int = self.k
        if k == 0:
            return None
        return self.kth_permutation(self.k - 1)

    def next_item(self, L=None) -> Any:
        k: int = self.k
        if L:
            k: int = self.id_of_permutation(L)
        if k + 1 == self.facn:
            return None
        return self.kth_permutation(k + 1)


##################################
N = int(input())
P = [int(a) for a in input().split()]
mut = Permutation(P)
print(*mut.previous_item())

######prefix######
# Lib_permutation_順列
##############end##############
