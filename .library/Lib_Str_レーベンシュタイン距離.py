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
# distance: O(∣S∣∣T∣)
# 最小の手順回数がK以下
# islowerK: O(min(∣S∣,∣T∣) * K)
#####################################
# https://algo-method.com/tasks/315
# https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_E
# https://atcoder.jp/contests/abc386/tasks/abc386_f

class Levenshtein:
    def __init__(self, S: str | list[str], T: str | list[str]) -> None:
        self.Type: type[str] | type[list[str]] = type(S)
        self.S: list[str] = list(S) if self.Type is str else S
        self.T: list[str] = list(T) if self.Type is str else T
        self.ls: int = len(S)
        self.lt: int = len(T)
        INF: int = max(self.ls, self.lt) + 1
        self.INF: int = INF
        self.length = INF

    def distance(self) -> int:
        """O(|S||T|)"""
        assert self.ls * self.lt <= 10**9, "maybe TLE"

        self.dp: list[list[int]] = [[self.INF] * (self.lt + 1) for _ in range(self.ls + 1)]
        dp: list[list[int]] = self.dp
        for i in range(self.ls + 1):
            dp[i][0] = i
        for j in range(self.lt + 1):
            dp[0][j] = j
        for i in range(self.ls):
            for j in range(self.lt):
                cost = 0 if S[i] == T[j] else 1
                dp[i + 1][j + 1] = min(
                    dp[i][j] + cost,
                    dp[i + 1][j] + 1,
                    dp[i][j + 1] + 1,
                )
        self.length: int = self.dp[self.ls][self.lt]
        return self.length

    def restore_ops(self) -> list[tuple[str, str, str]]:
        """Levenshtein の標準復元（編集操作列）"""
        S, T = self.S, self.T
        dp = self.dp
        i, j = self.ls, self.lt

        ops = []  # (operation, char_from_S, char_from_T)

        while i > 0 or j > 0:
            # ---------------------------------------------
            # ① 両方 1 つ戻れる場合（match or replace）
            # ---------------------------------------------
            if i > 0 and j > 0:
                cost = 0 if S[i - 1] == T[j - 1] else 1
                if dp[i][j] == dp[i - 1][j - 1] + cost:
                    if cost == 0:
                        ops.append(("match", S[i - 1], T[j - 1]))
                    else:
                        ops.append(("replace", S[i - 1], T[j - 1]))
                    i -= 1
                    j -= 1
                    continue

            # ---------------------------------------------
            # ② delete（S 側の文字を削除）
            # ---------------------------------------------
            if i > 0 and dp[i][j] == dp[i - 1][j] + 1:
                ops.append(("delete", S[i - 1], None))
                i -= 1
                continue

            # ---------------------------------------------
            # ③ insert（T 側の文字を挿入）
            # ---------------------------------------------
            if j > 0 and dp[i][j] == dp[i][j - 1] + 1:
                ops.append(("insert", None, T[j - 1]))
                j -= 1
                continue

            # ---------------------------------------------
            # ④ ここに来るのは通常ありえない（DP が壊れている）
            # ---------------------------------------------
            raise RuntimeError("DP restore failed")

        ops.reverse()
        return ops

    def islowerK(self, K:int) -> bool:
        """distance <= K"""
        """O(min(|S|, |T|) * K)"""
        ls, lt, S, T = self.ls, self.lt, self.S, self.T
        assert min(ls, lt) * K <= 10**8, "maybe TLE"
        if ls > lt:
            ls, lt, S, T = lt, ls, T, S
        if lt - ls > K:
            return False

        dp:list[int] = [self.INF] * K + list(range(K + 1))
        for i in range(1, ls + 1):
            ndp:list[int] = [self.INF] * (2 * K + 1)
            for d in range(2 * K + 1):
                j = i + d - K
                if j < 0:
                    continue
                if j > lt:
                    break
                if j > 0:
                    ndp[d] = min(ndp[d], dp[d] + (S[i - 1] != T[j - 1]))
                if j - i < K:
                    ndp[d] = min(ndp[d], dp[d + 1] + 1)
                if j > 0 and j - i > -K:
                    ndp[d] = min(ndp[d], ndp[d - 1] + 1)
            dp = ndp

        return dp[lt - ls + K] <= K

#####################
K = int(input())
S = input()
T = input()

ldiff = Levenshtein(S, T)
print(ldiff.distance())
print(ldiff.restore_ops())
print("Yes" if ldiff.islowerK(K) else "No")


######prefix######
# Lib_Str_レーベンシュタイン距離_Levenshtein_distance#
##############end##############
