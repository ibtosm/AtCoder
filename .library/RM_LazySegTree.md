# LazySegTreeライブラリー

## 普通の演算のモノイド

### RMinQ and RAQ

```
INF = 10 ** 18
op = min; e = INF;
mp = lambda f, x: f+x
cmp = lambda f, g: f+g
id = 0
```

### RMaxQ and RAQ

```
INF = 10 ** 18
op = max; e = -INF;
mp = lambda f, x: f+x
cmp = lambda f, g: f+g
id = 0
```

### RSumQ and RAQ

monoidは(区間合計, 区間幅)

```
op = lambda x, y: (x[0]+y[0], x[1]+y[1]); e = (0,0)
mp = lambda f, x: (x[0]+f*x[1], x[1])
cmp = lambda f, g: f+g
id = 0
```

### RMinQ and RUQ

```
INF = 10 ** 18
op = min; e = INF
mp = lambda f, x: x if f == INF else f
cmp = lambda f, g: g if f == INF
id = INF
```

### RMaxQ and RUQ

```
INF = 10 ** 18
op = max; e = -INF
mp = lambda f, x: x if f == -INF else f
cmp = lambda f, g: g if f == -INF
id = -INF
```

### RSumQ and RUQ

```
op = lambda x, y: (x[0]+y[0], x[1]+y[1]); e = (0, 0)
mp = lambda f, x: x if f == INF else (f*x[1], x[1])
cmp = lambda f, g: g if f == INF
id = INF
```

### 基本のmax_rightの使い方

- https://atcoder.jp/contests/practice2/tasks/practice2_j

### 区間の右と左の情報を持って、区間の情報を集約するタイプ

- https://atcoder.jp/contests/abc415/tasks/abc415_f

### AAL Contest 001: Let's use segtree!

- https://atcoder.jp/contests/aalc001/tasks

```

```
