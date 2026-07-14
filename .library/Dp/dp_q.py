####################
# EDPC Q Flowers
# https://atcoder.jp/contests/dp/tasks/dp_q/
####################
# セグメント木を使う

# Segment Tree
# 一点更新・区間集約

class SegmentTree:  # 初期化処理
    # f    : SegmentTreeにのせるモノイド
    # e   : fに対する単位元
    def __init__(self, init, f, ie):
        self._f = f
        self._ie = ie
        if type(init) == int:
            init = [ie] * init
        self._n = len(init)
        self._log = (self._n - 1).bit_length()  # seg木の深さ
        self._size = 1 << self._log     # seg木のサイズ
        # seg木の初期化
        self._dat = [ie] * self._size + init + [ie] * (self._size - len(init))
        for i in range(self._size-1, 0, -1):
            self._update(i)


    def update(self, i, x):
        # one point update
        i += self._size
        self._dat[i] = x
        while i > 0:    # 層をのぼりながら値を更新 indexが0になれば終了
            i >>= 1     # 1つ上の層のインデックス(完全二分木における親)
            # 下の層2つの演算結果の代入(完全二分木における子同士の演算)
            self._update(i)


    def getvalue(self, i):
        return self._dat[i + self._size]


    def query(self, l, r):
        # モノイドでは可換律は保証されていないので演算の方向に注意
        l += self._size  # 1番下の層におけるインデックス
        r += self._size  # 1番下の層におけるインデックス
        # 左側の答えと右側の答えを初期化
        lret, rret = self._ie, self._ie
        while l < r:    # lとrが重なるまで上記の判定を用いて演算を実行
            # 左が子同士の右側(lが奇数)(lの末桁=1)ならば、dat[l]を演算
            if l & 1:
                lret = self._f(lret, self._dat[l])
                l += 1
            # 右が子同士の右側(rが奇数)(rの末桁=1)ならば、dat[r-1]を演算
            if r & 1:
                r -= 1
                rret = self._f(self._dat[r], rret)
            l >>= 1
            r >>= 1
        return self._f(lret, rret)


    def _update(self, i):
        # 下の層2つの演算結果の代入(完全二分木における子同士の演算)
        self._dat[i] = self._f(self._dat[i*2], self._dat[i*2+1])


####################################

# Range Maximum Query
def op(x, y):
    return max(x, y)
ie = -float('inf')

#######################################

n = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

dp = SegmentTree([0] * (n+2), op, ie)

# dp[i][j] i番目まで見て最後に取った高さhがjである場合の最大価値
# dp[i][hi] = max( dp[i-1][j] + ai  (j<hi) )  i番目を使うとき
#               -> セグメント木を使う

for i, (hi, ai) in enumerate(zip(h, a)):
    dp.update(hi, dp.query(0, hi) + ai)

print(dp.query(0, n+1))
