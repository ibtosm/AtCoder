##############name##############
# 巡回セールスマン問題
######description######
# 巡回セールスマン問題
######body######
# bitDP
# dp[s][i]  集合sに行って、今iにいる場合の最小距離

INF = 1000_000_000
N, M = map(int, input().split())
# 辺の情報
dist: list[list[int]] = [[INF] * N for _ in range(N)]
for fm in range(N):
    dist[fm][fm] = 0
for _ in range(m):
    fm, to, d = map(int, input().split())
    fm -= 1
    to -= 1
    dist[fm][to] = d


# 距離関数
def d(fm, to):
    if dist[fm][to] != INF:
        return dist[fm][to]
    else:
        # 何か変則処理
        # ex. dist[fm][to] = abs(a-p) + abs(b-q) + max(0, r-c)
        return dist[fm][to]


# dp[s][i]  集合sに行って、今iにいる場合の最小距離
# 最初は0だがsにはカウントしない
dp: list[list[int]] = [[INF] * N for _ in range(1 << N)]
for first in range(N):
    dp[1 << first][first] = d(fm=0, to=first)

for s in range(1, 1 << N):
    for fm in range(N):
        if (not s >> fm & 1) or (dp[s][fm] == INF):
            # fmがsに無い場合->スキップ
            # 到達距離がINF->スキップ
            continue
        for to in range(N):
            if s >> to & 1:
                continue  # すでにtoがsにいる場合->スキップ
            next_s: int = s | (1 << to)  # toを追加した状態
            dp[next_s][to] = min(dp[next_s][to], dp[s][fm] + d(fm, to))

ret: int = dp[-1][0]
print(-1 if ret == INF else ret)


######prefix######
# Lib_A_巡回セールスマン問題_TSP_bitDP
##############end##############
