######title######
# 数直線上の距離の合計
######subtitle######
# 数直線上の点を一か所に集める時のコスト

##############name##############
# 数直線上の距離の合計
######description######
# 数直線上の点を一か所に集める時のコスト
######body######

from bisect import bisect

class points_diffs:
    def __init__(self, A:list):
        self.X = sorted(A)
        self.RX = [0]
        self.N = len(A)
        for ai in self.X:
            self.RX.append(self.RX[-1] + ai)

    def cost_left(self, x):
        """
        xの左側の点をxに持ってくるコスト
        """
        u = bisect(self.X, x)
        return u*x - self.RX[u]

    def cost_right(self, x):
        """
        xの右側の点をxに持ってくるコスト
        """
        u = bisect(self.X, x)
        return self.RX[-1] - self.RX[u] - (self.N-u) * x

    def cost(self, x):
        return self.cost_left(x) + self.cost_right(x)

    def minvalue(self, f):
        """xコストに関する最小値"""
        """"""
        l = min(self.A)
        r = max(self.A)
        while r - l > 2:
            _l = l + (r-l)//3
            _r = r - (r-l)//3
            if f(_l) > (_r):
                l = _l
            else:
                r = _r
        return min(f(l), f(r))

A = [0, 1, 2, 3, 3, 5]
pd = points_diffs(A)
d = 1
print(pd.minvalue(lambda x: pd.cost_left(x) + pd.cost_right(x+d)))

######prefix######
# Lib_A_数直線上の距離の合計
##############end##############
