# XOR の性質
## 定義
- a = 0, b = 0 -> a⊕b = 0
- a = 1, b = 0 -> a⊕b = 1
- a = 0, b = 1 -> a⊕b = 1
- a = 1, b = 1 -> a⊕b = 0

## 可換
- a⊕b == b⊕a

## 結合
- (a ⊕ b) ⊕ c == a ⊕ (b ⊕ c)

## 逆元
xの逆元はx
- a ⊕ x ⊕ x = a
- a ⊕ x = b ⊕ x  ⇔ a = b
- a != b ⇔ a ⊕ x != b ⊕ x

## 通常和との関係1
桁の繰上りがxorにはない
- a ⊕ b ≦ a + b
- 一致するときは繰上りがないつまり同じ桁に1,1となることはない

## 通常和との関係2
a + b = a ⊕ b + 2*(a & b)

## 任意の偶数 n についてn ^ (n+1) = 1
隣同士のxorは1
## 0^1^...^(x-1)^x 累積xor
累積xorはmod4で値が決まる
```
def g(x):
    return [x, 1, 1^x, 0][x%4]
```

## 大小関係
任意の非負整数 x, y, z (x < y < z) に対して、
min(x⊕y ,y⊕z) < x ⊕ z
https://atcoder.jp/contests/abc308/tasks/abc308_g

