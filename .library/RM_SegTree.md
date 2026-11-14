# DPライブラリー

## 普通の演算のモノイド

### Range MAX

INF = 10**18
op = max; e = -INF

### Range MIN

INF = 10**18
op = max; e = -INF

### Range SUM

op = lambda x, y: x + y; e = 0

### Range Prod

op = lambda x, y: x * y; e = 1

### Range Xor

op = lambda x, y: x ^ y; e = 0

### Range GCD

import math

def op(x, y):
if x == 0: return y
if y == 0: return x
return math.gcd(x, y)
e = 0

## 区間の右と左の情報を持って、区間の情報を集約するタイプ

### https://atcoder.jp/contests/abc415/tasks/abc415_f

### https://atcoder.jp/contests/abc415/submissions/67879850
