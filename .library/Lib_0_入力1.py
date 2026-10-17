##############name##############
# N = int(input())
######description######
# 整数Nの読み込み
######body######
N = int(input())
######prefix######
# nin
##############end##############

##############name##############
# N = / A =
######description######
# 整数N, リストAの読み込み
######body######
N = int(input())
A = list(map(int, input().split()))
######prefix######
# nain
##############end##############

##############name##############
# S=input()
######description######
# 文字列Sの読み込み
######body######
S = list(input())
######prefix######
# sin
##############end##############

##############name##############
# N, M =
######description######
# 整数N, Mの読み込み
######body######
N, M = map(int, input().split())
######prefix######
# nmin
##############end##############

##############name##############
# N, Q =
######description######
# 整数N, Qの読み込み
######body######
N, Q = map(int, input().split())
######prefix######
# nqin
##############end##############

##############name##############
# H, W =
######description######
# 整数h, wの読み込み
######body######
H, W = map(int, input().split())
######prefix######
# hwin
##############end##############

##############name##############
# A=list(map(int, input().split()))
######description######
# リストの読み込み
######body######
A = list(map(int, input().split()))
######prefix######
# ain
##############end##############

##############name##############
# B=list(map(int, input().split()))
######description######
# リストの読み込み
######body######
B = list(map(int, input().split()))
######prefix######
# bin
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

##############name##############
# 0インデックスu, v
######description######
# 0-indexed u, v
######body######
u -= 1; v -= 1
######prefix######
# u -= 1; v -= 1
##############end##############
