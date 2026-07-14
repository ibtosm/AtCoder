##############name##############
# 尺取り
######description######
# Lib_尺取り
######body######
######################################################################
# The Smallest Window I
# 長さNの数列a1,a2,a3,...,aNと整数Sが与えられます。
# 要素の総和がS以上となる連続する部分列のうち、
# 最も短いものの長さ（smallest window length）を求めてください。
# ただし、そのような部分列が存在しない場合は 0 と報告してください。
# https://onlinejudge.u-aizu.ac.jp/problems/DSL_3_A
######################################################################

N, S = map(int, input().split())
A = list(map(int, input().split()))
INF = 2*N
ret = INF

l, r, now = 0, 0, 0
while True:
    while r < N and now < S:
        now += A[r]
        r += 1
    if now >=S:
        ret = min(ret, r - l)
        now -= A[l]
        l += 1
    else:
        break

if ret == INF:
    print(0)
else:
    print(ret)

######################################################################
# The Smallest Window II
# 長さNの数列a1,a2,a3,...,aNと整数Kが与えられます。
# 1からKまでの整数1, 2, ...,Kをすべて含む連続する部分列のうち、
# 最も短いものの長さ（smallest window length）を求めてください。
# ただし、そのような部分列が存在しない場合は 0 と報告してください。
# https://onlinejudge.u-aizu.ac.jp/problems/DSL_3_B
######################################################################

N, K = map(int, input().split())
A = list(map(int, input().split()))
now_each_counter = [0] * (K+1)
now_total_counter = 0
l, r = 0, 0
INF = 2*N
ret = INF
while l < N:
    while r < N and now_total_counter < K:
        ar = A[r]
        if ar <= K:
            now_each_counter[ar] += 1
            if now_each_counter[ar] == 1:
                now_total_counter += 1
        r += 1
    if now_total_counter == K:
        ret = min(ret, r-l)
    al = A[l]
    if al <= K:
        now_each_counter[al] -= 1
        if now_each_counter[al] == 0:
            now_total_counter -= 1
    l += 1
if ret == INF:
    print(0)
else:
    print(ret)

######################################################################
# The Number of Windows
# 長さNの数列a1,a2,a3,...,aNが与えられます。
# また, 次のような質問がQ個与えられます。
# i個目の質問では,整数x,iが与えられます。
# 各質問について1<=l<=r<=Nかつsum(al,al+1,...,ar-1,ar) <= xiを満たす整数
# (l,r)の組の個数を求めてください。
# https://onlinejudge.u-aizu.ac.jp/problems/DSL_3_C
######################################################################
N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))

def solv(x):
    l, r, ret = 0, 0, 0
    now = 0
    while l < N:
        while r < N and now <= x:
            now += A[r]
            r += 1
        if now > x:
            r -= 1
            now -= A[r]
        ret += r - l
        now -= A[l]
        l += 1
    return ret

for xi in X:
    print(solv(xi))

######################################################################
# Sliding Minimum Element
# 長さNの数列a1,a2,a3,...,aNと整数Lが与えられます。
# 長さLの連続する部分列すべてについて、
# 各部分列の中の最小の要素を先頭から順番に報告してください。
# 例えば、数列が{1,7,7,4,8,1,6} で、L が 3 の場合、
# 長さLの部分列は{1,7,7},{7,7,4},{7,4,8},{4,8,1},{8,1,6}となりますが、
# それぞれの部分列の最小値となる 1, 4, 4, 1, 1 を先頭の方から順番に出力してください。
# https://onlinejudge.u-aizu.ac.jp/problems/DSL_3_D
######################################################################
from heapq import heapify, heappop, heappush
N, L = map(int, input().split())
A = list(map(int, input().split()))
ret = []
que = []
heapify(que)
for i, ai in enumerate(A):
    heappush(que, (ai, i))
    if i < L-1: continue
    while que[0][1] <= i - L:
        heappop(que)
    ret.append(que[0][0])
print(*ret)

######prefix######
# Lib_O_尺取り
##############end##############
