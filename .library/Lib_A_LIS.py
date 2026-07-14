######title######
# 最長増加部分列

######subtitle######
# LIS(x, fg): xは数列で構築
# fg: 0:単調非減少, 1:単調増加
# LIS.length: 長さ
# LIS.restore: 数列

##############name##############
# LIS最長増加部分列
######description######
# Lib_LIS最長増加部分列
######body######
#####################################
# 最長増加部分列 dp[k]
# 今まで見た来たものの中で、単調増加(非減少)な部分列であって、
# 長さ k であるようなもののうち、その最後の要素の最小値
# 新しいアイテムuだったとき
# dp[k] < u となる一番右の列(k)を特定しその次のdp[k+1]を小さければ更新する
# rem: kに対して単調増加
from bisect import bisect_left, bisect_right


class LIS:
    """
    fg: 0:単調非減少, 1:単調増加
    dp: lis[i]: 列の長さiの最長部分列で最後の要素の最小値
    """

    def __init__(self, A: list, fg: int = 1):
        self.A = A
        self.N = n = len(A)
        self.length = 0
        self.res = res = [0] * n
        self.dp = dp = []

        for i, a in enumerate(A):
            pos = bisect_left(dp, a) if fg else bisect_right(dp, a)
            res[i] = pos + 1
            if len(dp) <= pos:
                dp.append(a)
                self.length += 1
            else:
                dp[pos] = a

    def __str__(self):
        ret = "------------------------------\n"
        ret += f"length   : {self.length}\n"
        ret += f"dp_table : {self.dp}\n"
        ret += f"res      : {self.res}\n"
        ret += f"originalA: {self.A}\n"
        ret += "------------------------------"

        return ret

    def restore(self):
        restore = []
        nw = self.length
        for i in range(self.N)[::-1]:
            if nw == self.res[i]:
                restore.append(self.A[i])
                nw -= 1
        restore.reverse()
        return restore


####################################

# N = 8
# A = [3, 1, 4, 1, 5, 9, 2, 10]
# lis = LIS(A)
# length___:_5
# dp_table_:_[1,_2,_5,_9,_10]
# res______:_[1,_1,_2,_1,_3,_4,_2,_5]


######prefix######
# Lib_LIS最長増加部分列
##############end##############
