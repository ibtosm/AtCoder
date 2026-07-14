######title######
# 文字列等の部分列の個数を数える
######subtitle######
# count_subsets(S): Sの部分列を数える
# CountSubsets(S,T): S,Tの共通した部分列を数える

##############name##############
# 部分列の個数
######description######
# Lib_Substrings_count
######body######

def count_subsets(S, mod=10**9+7):
    """
    部分列（連続でない）の個数を数える
    空集合を含める
    """
    if type(S) == str:
        S = [ord(si)-ord('a') for si in S]
    ls = len(S)
    maxs = max(S)
    pps = [[-1] * (maxs+1) for _ in range(ls+1)]
    for i, si in enumerate(S):
        for j in range(maxs+1):
            pps[i+1][j] = pps[i][j]
            if si == j: pps[i+1][j] = i

    dp = [0] * (ls+1)
    dp[0] = 1
    for i, si in enumerate(S):
        dp[i+1] = dp[i]
        if pps[i][si] == -1:
            dp[i+1] += dp[i]
        else:
            dp[i+1] += dp[i] - dp[pps[i][si]]
        dp[i+1] %= mod

    return dp[ls]


#####################


# https://atcoder.jp/contests/past202206-open/tasks/past202206_k
class CountSubsets:
    def __init__(self, S, T, mod) -> None:
        self.S = S
        self.T = T
        self.ls = n = len(S)
        self.lt = m = len(T)
        self.dp = [[0]*(m+1) for _ in range(n+1)]
        self._adj()
        self.mod = mod
        self.scS, self.ppS = self._substr_count(self.S)
        self.scT, self.ppT = self._substr_count(self.T)
        self.scbothST = self._substr_count_both()

    def _adj(self):
        mn = min(min(self.S), min(self.T))
        self.S = [u - mn for u in self.S]
        self.T = [u - mn for u in self.T]
        self.Max = max(max(self.S), max(self.T))

    def _pp(self, S):
        ls = len(S)
        pps = [[-1] * (self.Max+1) for _ in range(ls+1)]
        for i, si in enumerate(S):
            for j in range(self.Max+1):
                pps[i+1][j] = pps[i][j]
                if si == j: pps[i+1][j] = i
        return pps

    def _substr_count(self, S):
        mod = self.mod
        pps = self._pp(S)
        ls = len(S)
        dp = [0] * (ls+1)
        dp[0] = 1
        for i, si in enumerate(S):
            dp[i+1] = dp[i]
            if pps[i][si] == -1:
                dp[i+1] += dp[i]
            else:
                dp[i+1] += dp[i] - dp[pps[i][si]]
            dp[i+1] %= mod

        return dp[ls], pps

    def _substr_count_both(self):
        S, T = self.S, self.T
        ls, lt = self.ls, self.lt
        pps, ppt = self.ppS, self.ppT
        dp = [[0] * (lt+1) for _ in range(ls+1)]
        for i in range(ls+1):
            dp[i][0] = 1
        for j in range(lt+1):
            dp[0][j] = 1

        for i, si in enumerate(S):
            for j, tj in enumerate(T):
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j]
                if si != tj: continue
                pi, pj = pps[i][si], ppt[j][tj]
                if pi != -1 and pj != -1:
                    dp[i+1][j+1] += dp[i][j] - dp[i][pj] - dp[pi][j] + dp[pi][pj]
                elif pi != -1 and pj == -1:
                    dp[i+1][j+1] += dp[i][j] - dp[pi][j]
                elif pi == -1 and pj != -1:
                    dp[i+1][j+1] += dp[i][j] - dp[i][pj]
                else:
                    dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= self.mod
        return dp[ls][lt]

#####################

mod = 998244353
s = input()
t = input()
s = [ord(si)-ord('a') for si in s]
t = [ord(si)-ord('a') for si in t]
cs = CountSubsets(s, t, mod)
print((cs.scS+cs.scT-cs.scbothST - 1)%mod)

######prefix######
# Lib_部分列個数_subsetcount#
##############end##############

