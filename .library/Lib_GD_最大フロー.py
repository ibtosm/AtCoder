######title######
# 最大フロー
######subtitle######
# MFGraph: 各辺(u,v)には容量capが設定、始点sから終点tへの最大流を求める
# O(∣V∣**2・∣E∣), O(∣V+E∣・E**0.5 辺が全て1の時)

##############name##############
# 最大フロー
######description######
# 最大フローO(∣V∣**2・∣E∣)
######body######

# 最大流問題
# 始点sと終点tが区別された有向グラフ
# 各辺(u,v)には容量c(u,v)が設定されており、超えないフローが流れます。
# 始点sから終点tへの最大流を求める。
#
# Dinic's algorithm
# 幅優先探索で水を流す向きをざっと決める．
# 深さ優先探索で決められた向きで流せる経路を探し，水を流す．
# 流せなくなったら1に戻る.
# O(∣V∣**2・∣E∣), O(∣V+E∣・E**0.5 辺が全て1の時)
# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_6_A

# https://github.com/not522/ac-library-python/blob/master/atcoder/maxflow.py
# https://github.com/atcoder/ac-library/blob/master/document_ja/maxflow.md
# Edge
# __init__(n)
# add_edge(src, dst, cap)
# flow(s, t, flow_limit)
# (1) 頂点 から へ流せる限り流し、流せた量を返す。
# (2) 頂点 から へ流量 flow_limit に達するまで流せる限り流し、流せた量を返す。
# change_edge(i, newcap, newflow)
# edges(): 辺の情報
# min_cut(s)
from atcoder.maxflow import MFGraph

#############
n, m = map(int, input().split())
mf = MFGraph(n)
for _ in range(m):
    a, b, e = map(int, input().split())
    a -= 1; b -= 1
    mf.add_edge(a, b, e)

print(mf.max_flow(0, n-1))

######prefix######
# Lib_GD_最大フロー_maximumflow_dinic
##############end##############
