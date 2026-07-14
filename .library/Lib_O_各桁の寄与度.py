##############name##############
# 各桁の寄与度
######description######
# 各桁の寄与度
# 356
######body######
def sum_digit(s, d=10, mod=-1):
    n = len(s)
    ret = 0

    pow_2 = [1]
    pow_d = [1]
    div = pow(d-2, mod - 2, mod)
    for _ in range(n):
        if mod == -1:
            pow_2.append(pow_2[-1] * 2)
            pow_d.append(pow_d[-1] * d)
        else:
            pow_2.append(pow_2[-1] * 2 % mod)
            pow_d.append(pow_d[-1] * d % mod)

    def _contribute(k):
        r = pow_2[n-1-k] * ((d-1)* pow_d[k] - pow_2[k])
        if mod == -1:
            r //= d-2
        else:
            r *= div
        return r


    for i, si in enumerate(s[::-1]):
        ret += _contribute(i) * int(si) % mod
    return ret % mod

mod = 998244353
s = input()
print(sum_digit(s, 10, mod))

######prefix######
# Lib_O_各桁の寄与度
##############end##############
