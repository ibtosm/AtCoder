######title######
# 最小費用流
######subtitle######
# MCFGraph: 各辺(u,v)には容量cap, が設定、始点sから終点tへの最小コストを求める
# O(F(∣V∣+∣E∣)log((∣V∣+∣E∣)))


##############name##############
# 最小費用流
######description######
# 最小費用流を算出するO(FElogV) ダイクストラ
######body######

# 最小費用流問題
# 各辺に容量とコストが設定されたフローネットワークにおいて、
# 始点s から終点t まで流量F のフローを流すための最小コストを求める
# Minimum Cost Flow : O(FElogV) ダイクストラ
# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_6_B
# https://atcoder.jp/contests/practice2/tasks/practice2_d

# https://github.com/not522/ac-library-python/blob/master/atcoder/mincostflow.py
# https://github.com/atcoder/ac-library/blob/master/document_ja/mincostflow.md
# Edge
# __init__(n)
# add_edge(src, dst, cap, cost)
# flow(s, t, flow_limit)
# (1) 頂点 から へ流せる限り流し、流せた量とコストを返す。
# (2) 頂点 から へ流量 flow_limit に達するまで流せる限り流し、流せた量とコストを返す。
# change_edge(i, newcap, newflow)
# edges(): 辺の情報
# min_cut(s)
from atcoder.mincostflow import MCFGraph

#############
n, m, f = map(int, input().split())
mf = MCFGraph(n)
for _ in range(m):
    u, v, cap, cost = map(int, input().split())
    mf.add_edge(u, v, cap, cost)

print(mf.min_cost_flow(0, n-1, f))

######prefix######
# Lib_GD_最小費用流_mincostflow
##############end##############
