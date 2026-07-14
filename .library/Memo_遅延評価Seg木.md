# 遅延評価セグメント木

## AtCoder Library Practice Contest K - Range Affine Range Sum
https://atcoder.jp/contests/practice2/tasks/practice2_k
```
mod = 998244353
bit = 30
msk = (1<<bit)-1
n, q = map(int, input().split())
A = list(map(int, input().split()))
A = [ai<<bit|1 for ai in A]

# 区間集約演算 *: G * G -> G の定義.
def op(x, y):
    xv, xlen = x>>bit, x&msk
    yv, ylen = y>>bit, y&msk
    r0 = (xv+yv)%mod
    r1 = (xlen+ylen)%mod
    return r0<<bit|r1

# op演算の単位元
e = 0

# 区間更新演算 ·: F · G -> G の定義.
def mapping(f,x):
    f0, f1 = f>>bit, f&msk
    sx, lx = x>>bit, x&msk
    r0 = (f0*sx + f1*lx)%mod
    r1 = lx
    return r0<<bit|r1

# 遅延評価演算 ·: F · F -> F の定義.
def composition(f, g):
    f0, f1 = f>>bit, f&msk
    g0, g1 = g>>bit, g&msk
    r0 = f0*g0%mod
    r1 = (f0*g1+f1)%mod
    return r0<<bit|r1

# 遅延評価演算の単位元
id = 1<<bit

sgt = LazySegmentTree(op, e, mapping, composition, id, A)

for _ in range(q):
    t, *qry = map(int, input().split())
    if t == 0:
        l, r, b, c = qry
        sgt.apply(l, r, b<<bit|c)
    else:
        l, r = qry
        ans = sgt.prod(l, r)
        print(ans>>bit)
```

## ACL Beginner Contest E - Replace Digits
https://atcoder.jp/contests/abl/tasks/abl_e

```
mod = 998244353
pow10 = [1]
pow1 = [0]
nw10 = 1
nw1 = 0
for _ in range(200000):
    nw1 += nw10
    nw1 %= mod
    nw10 = (nw10*10)%mod
    pow10.append(nw10)
    pow1.append(nw1)


# 区間集約演算 *: G * G -> G の定義
def op(tuple_a, tuple_b):
    na, la = tuple_a
    nb, lb = tuple_b
    return ((na*pow10[lb]+nb)%mod, la+lb)

# op演算の単位元
e = (0, 0)

# 区間更新演算 ·: F · G -> G の定義
def mapping(f, tuple_a):
    if f == -1:
        return tuple_a
    na, la = tuple_a
    return (pow1[la]*f%mod, la)


# 遅延評価演算 ·: F · F -> F の定義
def composition(f, g):
    if f==-1: return g
    return f

# 遅延評価演算の単位元
id = -1


#######################################################

n, q = map(int, input().split())
a = [(1, 1) for _ in range(n)]

sgt = LazySegmentTree(op, e, mapping, composition, id, a)
for _ in range(q):
    l, r, d = map(int, input().split())
    l -= 1
    sgt.apply(l, r, d)
    sgt.query(0, n)
    print(sgt.all_prod()[0])
```

## AtCoder Library Practice Contest L - Lazy Segment Tree
https://atcoder.jp/contests/practice2/tasks/practice2_l
0,1の数列：区間反転：区間転倒数集約
```
# 区間集約演算 *: G * G -> G の定義.
def op(x, y):
    invx, c0x, c1x = x
    invy, c0y, c1y = y
    return (invx+invy+c0y*c1x, c0x+c0y, c1x+c1y)

# op演算の単位元(反転数,区間内の０の数,区間内の１の数)
e = (0, 0, 0)

# 区間更新演算 ·: F · G -> G の定義.
def mapping(f, x):
    if f==0: return x
    inv, c0, c1 = x
    return (c1*c0 - inv, c1, c0)

# 遅延評価演算 ·: F · F -> F の定義.
def composition(f, g):
    return f ^ g

# 遅延評価演算の単位元
id = 0


#######################################################

n, q = map(int, input().split())
a = []
for i in map(int, input().split()):
    if i == 1:
        a.append((0, 0, 1))
    else:
        a.append((0, 1, 0))


sgt = LazySegmentTree(op, e, mapping, composition, id, a)

for _ in range(q):
    t, l, r = map(int, input().split())
    l -= 1
    if t == 1:
        sgt.apply(l, r, 1)
    else:
        ret = sgt.query(l, r)
        print(ret[0])

```

## 第13回 アルゴリズム実技検定 過去問 O - シフトとシフト
https://atcoder.jp/contests/past202212-open/tasks/past202212_o

```
n, d = map(int, input().split())
A = list(input().split())
bs = pow(10, d-1)
for i in range(n):
    x = [int(A[i])]
    for j in range(d-1):
        f, s = divmod(x[-1], bs)
        x.append(s*10+f)
    A[i] = x

# 区間集約演算 *: G * G -> G の定義.
def op(x, y):
    ret = [0] * d
    for i in range(d):
        ret[i] = x[i]^y[i]
    return ret

# op演算の単位元
e = [0] * d

# 区間更新演算 ·: F · G -> G の定義.
def mapping(f,x):
    ret = [0] * d
    for i in range(d):
        ret[(i-f)%d] = x[i]
    return ret

# 遅延評価演算 ·: F · F -> F の定義.
def composition(f, g):
    return (f+g)%d

# 遅延評価演算の単位元
id = 0

sgt = LazySegmentTree(op, e, mapping, composition, id, A)
sft = 0
for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        sft = (sft + q[1]) % n
    elif q[0] == 2:
        l, r, y = q[1:]
        l -= 1
        l += sft; r += sft
        l %= n; r %= n
        if l < r:
            sgt.apply(l, r, y)
        else:
            sgt.apply(0, r, y)
            sgt.apply(l, n, y)
    else:
        l, r = q[1:]
        l -= 1
        l += sft; r += sft
        l %= n; r %= n
        if l < r:
            ret = sgt.prod(l, r)[0]
        else:
            ret = sgt.prod(0, r)[0]
            ret ^= sgt.prod(l, n)[0]
        print(ret)
```