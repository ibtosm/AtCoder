######title######
# 最長共通部分列
######subtitle######
# LCS(S, T): SとTでクラスを構築
# len: LCSの長さ
# str: 最長共通部分列を構築

##############name##############
# LCS最長共通部分列
######description######
# Lib_LCS最長共通部分列
######body######
#####################################
# LCS(longest common sequence)
# 部分列で最長の共通のもの
#####################################
# https://atcoder.jp/contests/dp/tasks/dp_f

# dp[i+1][j+1]:= s の i 文字目までと t の j 文字目まででの LCS の長さ
class LCS:
    def __init__(self, S, T) -> None:
        self.Type = type(S)
        if self.Type is str:
            S = list(S)
            T = list(T)
        self.S = S
        self.T = T
        self.ls = n = len(S)
        self.lt = m = len(T)
        self.dp = [[0]*(m+1) for _ in range(n+1)]
        dp = self.dp
        for i, si in enumerate(S):
            for j, tj in enumerate(T):
                if si == tj:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    def __len__(self):
        # LCSの長さ
        return self.dp[self.ls][self.lt]

    def __str__(self):
        # 復元
        ret = []
        i, j = self.ls, self.lt
        dp = self.dp
        while i and j:
            # (i-1, j) -> (i, j) と更新されていた場合
            if dp[i][j] == dp[i-1][j]:
                i -= 1   # DP の遷移を遡る
            # (i, j-1) -> (i, j) と更新されていた場合
            elif dp[i][j] == dp[i][j-1]:
                j -= 1   # DP の遷移を遡る
            # (i-1, j-1) -> (i, j) と更新されていた場合
            else:
                ret.append(self.S[i-1])
                # このとき s[i-1] == t[j-1] なので、t[j-1] + res でも OK
                i -= 1; j -= 1   # DP の遷移を遡る
        ret = ret[::-1]
        if self.Type is str: ret = ''.join(ret)
        return ''.join(ret)


#####################
#s = list(input())
#t = list(input())
s = '948640'
t = '540820'
lcs = LCS(s, t)
print(len(lcs))
print(lcs)

######prefix######
# Lib_LCS最長共通部分列#
##############end##############
