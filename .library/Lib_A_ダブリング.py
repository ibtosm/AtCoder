######title######
# ダブリング
######subtitle######
# f(i): 状態iからの１回の遷移先を定義
# doubbling(): ダブリングを構築
# fk(i, k): 状態iからk回の遷移先

##############name##############
# ダブリング
#discription#
# ダブリング
######body######

# https://atcoder.jp/contests/abc167/tasks/abc167_d

maxdeg = 100
n, k = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))

def f(i):
    # 1回の遷移
    return A[i]

def doubbling():
    dp = [[0] * n for _ in range(maxdeg)]
    for i in range(n):
        dp[0][i] = f(i)

    for t in range(1, maxdeg):
        for i in range(n):
            dp[t][i] = dp[t-1][dp[t-1][i]]
    return dp

dp = doubbling()

def fk(i, k):
    # iからk回遷移した時の結果
    for d in range(maxdeg):
        if k >> d & 1: i = dp[d][i]
    return i

print(fk(0, k)+1)

######prefix######
# Lib_A_ダブリング_doubbling
##############end##############
