##############name##############
# n=intinput
######description######
# 整数nの読み込み
######body######
N = int(input())
######prefix######
# nin
##############end##############


##############name##############
# nainput
######description######
# 整数nの読み込み
######body######
N = int(input())
A = list(map(int, input().split()))
######prefix######
# nain
##############end##############

##############name##############
# s=input
######description######
# 文字列sの読み込み
######body######
S = list(input())
######prefix######
# sin
##############end##############

##############name##############
# n,m=map(int, input().split())
######description######
# 整数n, mの読み込み
######body######
N, M = map(int, input().split())
######prefix######
# n, m=map
##############end##############

##############name##############
# h,w=map(int, input().split())
######description######
# 整数h, wの読み込み
######body######
H, W = map(int, input().split())
######prefix######
# h, w=map
##############end##############

##############name##############
# a=list(map(int, input().split()))
######description######
# リストの読み込み
######body######
A = list(map(int, input().split()))
######prefix######
# a =list
##############end##############

##############name##############
# edges
######description######
# edges
######body######
G = [[] for _ in range(${1:N})]
for _ in range(${2:M}):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

######prefix######
# G =
##############end##############

##############name##############
# edgesweighted
######description######
# edges(重み付き)
######body######
G = [[] for _ in range(${1:N})]
for _ in range(${2:M}):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    G[a].append((b, w))
    G[b].append((a, w))

######prefix######
# G = w
##############end##############

##############name##############
# 0インデックスa, b
######description######
# 0-indexed a, b
######body######
a -= 1; b -= 1
######prefix######
# a -= 1; b -= 1
##############end##############

##############name##############
# 0インデックスx, y
######description######
# 0-indexed x, y
######body######
x -= 1; y -= 1
######prefix######
# x -= 1; y -= 1
##############end##############
