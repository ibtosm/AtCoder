######title######
# Zアルゴリズム
######subtitle######
# z_altp: SとS[i:]の接頭辞が一致する長さのリスト

##############name##############
# Zアルゴリズム
######description######
# Zアルゴリズム
# S と S[i:]が接頭辞が一致する長さ
######body######

# Zアルゴリズム
# S と S[i:]が接頭辞が一致する長さ
# https://snuke.hatenablog.com/entry/2014/12/03/214243
def z_algo(S):
    n = len(S)
    A = [n] + [0] * (n-1)
    i, j = 1, 0
    while i < n:
        while i+j < n and S[j] == S[i+j]:
            j += 1
        A[i] = j
        if not j:
            i += 1
            continue
        k = 1
        while n-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k
    return A

s = input()
ret = z_algo(s)

# s = 'abcbcba'
# ret = z_algo(s)
# for i in range(len(s)):
#     print(i, ret[i], s, s[i:])
# 0 7 abcbcba abcbcba
# 1 0 abcbcba bcbcba
# 2 0 abcbcba cbcba
# 3 0 abcbcba bcba
# 4 0 abcbcba cba
# 5 0 abcbcba ba
# 6 1 abcbcba a

######prefix######
# Lib_STr_Zalgorithm
##############end##############
