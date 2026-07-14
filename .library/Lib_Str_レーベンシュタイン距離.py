######title######
# レーベンシュタイン距離
######subtitle######
# Levenshtein: 削除・挿入・変更により文字列を一致させる最小の手順回数

##############name##############
# レーベンシュタイン距離
######description######
# Lib_レーベンシュタイン距離
######body######

#####################################
# レーベンシュタイン距離 文字列の近似度
# 文字削除・挿入・変更により文字列を一致させる最小の手順回数
# distance: O(max(∣S∣,∣T∣))
# 最小の手順回数がK以下
# islowerK: O(min(∣S∣,∣T∣), K)
#####################################
# https://algo-method.com/tasks/315
# https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_E
# https://atcoder.jp/contests/abc386/tasks/abc386_f

class Levenshtein:
    def __init__(self, S:str|list, T:str|list) -> None:
        self.Type = type(S)
        self.S:list = list(S) if self.Type is str S
        self.T:list = list(T) if self.Type is str T
        self.ls:int = len(S)
        self.lt:int = len(T)
        self.INF :int= max(self.ls, self.lt) + 1

    def distance(self):
        """O(|S||T|)"""
        self.dp = [[self.INF]*(self.lt+1) for _ in range(self.ls+1)]
        dp = self.dp
        for i in range(self.ls):
            dp[i][0] = i
        for j in range(self.lt):
            dp[0][j] = j
        for i in range(self.ls):
            for j in range(self.lt):
                if S[i] == T[j]:
                    dp[i+1][j+1] = min(dp[i][j]  , dp[i+1][j]+1, dp[i][j+1]+1)
                else:
                    dp[i+1][j+1] = min(dp[i][j]+1, dp[i+1][j]+1, dp[i][j+1]+1)
        self.length = self.dp[self.ls][self.lt]
        return self.length

    def restore(self):
        # 復元
        ret = []
        i, j = self.ls, self.lt
        dp = self.dp
        while i and j:
            # (i-1, j) -> (i, j) と更新されていた場合
            if dp[i][j] == dp[i-1][j]:
                i-=1   # DP の遷移を遡る
            # (i, j-1) -> (i, j) と更新されていた場合
            elif dp[i][j] == dp[i][j-1]:
                j-=1   # DP の遷移を遡る
            # (i-1, j-1) -> (i, j) と更新されていた場合
            else:
                ret.append(self.S[i-1])
                # このとき s[i-1] == t[j-1] なので、t[j-1] + res でも OK
                i-=1
                j-=1   # DP の遷移を遡る
        ret = ret[::-1]
        return ''.join(ret) if self.Type is str else ret

    def islowerK(self, K):
        """distance <= K"""
        """O(min(|S|, |T|), K)"""
        ls, lt, S, T = self.ls, self.lt, self.S, self.T
        if ls > lt: ls, lt, S, T = lt, ls, T, S
        if lt - ls > K: return False

        dp = [self.INF] * K + list(range(K+1))
        for i in range(1, ls+1):
            ndp = [self.INF] * (2*K+1)
            for d in range(2*K+1):
                j = i + d - K
                if j < 0: continue
                if j > lt: break
                if j>0:
                    ndp[d] = min(ndp[d], dp[d] + (S[i-1] != T[j-1]))
                if j-i<K:
                    ndp[d] = min(ndp[d], dp[d+1] + 1)
                if j>0 and j-i>-K:
                    ndp[d] = min(ndp[d], ndp[d-1] + 1)
            dp = ndp

        return dp[lt-ls+K] <= K

#####################
K = int(input())
S = input()
T = input()

ldiff = Levenshtein(S, T)
print(ldiff.distance())
print('Yes' if ldiff.islowerK(K) else 'No')


######prefix######
# Lib_Str_レーベンシュタイン距離_Levenshtein_distance#
##############end##############
