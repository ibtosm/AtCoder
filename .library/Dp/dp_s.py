####################
# EDPC S DigitSum
# https://atcoder.jp/contests/dp/tasks/dp_s/
####################
# 桁DP

mod = 1000000007

k = input()
d = int(input())

deg = len(k)

# dp[i][res][0] 数がk以下に未確定で和の余りがres
# dp[i][res][1] 数がk以下に確定で和の余りがres

dp_0 = [0] * d
dp_1 = [0] * d
dp_0[0] = 1

for i, ki in enumerate(k):
    ki = int(ki)
    _dp_0 = [0] * d
    _dp_1 = [0] * d
    for res in range(d):
        for digit in range(10):
            fmres = (res - digit) % d
            # 桁が未確定のものからの遷移
            if ki == digit: # 未確定のまま
                _dp_0[res] += dp_0[fmres]
            elif ki > digit: # 確定へ
                _dp_1[res] += dp_0[fmres]
            # 桁が確定しているものからの遷移
            _dp_1[res] += dp_1[fmres]
        _dp_0[res] %= mod
        _dp_1[res] %= mod
    dp_0 = _dp_0[:]
    dp_1 = _dp_1[:]


ret = (dp_0[0] + dp_1[0] - 1) % mod
print(ret)
