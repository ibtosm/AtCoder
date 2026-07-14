######title######
# 回文
######subtitle######
# Palindrome: 文字列の中に含まれる回文を取得する O(N)
# OddStrRadius(c): 文字列S[c]を中心とした奇数列の最大の回文の半径
# EvenStrRadius(c): 文字列S[c]S[c+1]を中心とした偶数列の最大の回文の半径
# isPalindrome(c): 文字列S[l:r]が回文かどうか反転

##############name##############
# 回文
######description######
# 回文クラス
######body######
# https://atcoder.jp/contests/indeednow-finalb-open/tasks/indeednow_2015_finalb_c

class Palindrome:
    def __init__(self, S):
        self.L = len(S)
        self.S = S
        self.DL = 2 * self.L - 1
        _S = [0] * self.DL; _S[::2] = S
        self.DS = _S
        self.Mresult = self.manacher()

    def manacher(self):
        # 偶数長含めた回文の長さを求める
        # R[2*i] = L: S[i]を中心とする奇数長の最大回文の半径
        # R[2*i+1] = L: S[i:i+2]を中心とする偶数長の最大回文の半径
        # ダミー文字を挟むが、各 R[i] は実際の回文の文字列長と一致する
        L = self.DL; _S= self.DS
        R = [0] * L; i = 0; j = 0
        while i < L:
            while i >= j and i + j < L and _S[i-j] == _S[i+j]: j += 1
            R[i] = j; k = 1
            while (i >= k) and (i + k < L) and (k + R[i-k] < j):
                R[i + k] = R[i - k]; k += 1
            i += k; j -= k
        return R

    def OddStrRadius(self, c):
        pos = 2*c
        if pos >= self.DL: return -1
        r = (self.Mresult[pos] + 1) // 2
        return r

    def EvenStrRadius(self, c):
        pos = 2*c + 1
        if pos >= self.DL: return -1
        r = self.Mresult[pos] // 2
        return r

    def isPalindrome(self, l, r):
        """ 開区間[l,r)が回文か"""
        d = (r-l+1)//2
        c = l+d-1
        if (r-l)%2:
            return d <= self.OddStrRadius(c)
        return d <= self.EvenStrRadius(c)


n = int(input())
S = input()

pd = Palindrome(S)

######prefix######
# Lib_Str_回文_Palindrome
##############end##############
