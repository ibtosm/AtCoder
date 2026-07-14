
```
ret = 0

def dfs(bit, xo):
    global ret
    if bit == 0:
        ret = max(ret, xo)
        return

        nxtxo = xo ^ a[i][j]
        nxtbit = bit - (1<<i) - (1<<j)
        dfs(nxtbit, nxtxo)

dfs((1<<(2*n))-1, 0)
print(ret)
```
