######title######
# nCr剰余
######subtitle######
# 数え上げをmodで行う

##############name##############
# nCr
######description######
# nCr剰余
######body######


#####################################
# nCr % 998244353
# http://zakii.la.coocan.jp/enumeration/10_balls_boxes.htm
#####################################
class Combination:
    def __init__(self, maxn:int=10**6, mod:int=998244353) -> None:
        self.mod = mod
        self.maxn = maxn
        _maxn = maxn + 1
        fac, facinv, inv = [1]*_maxn, [1]*_maxn, [1]*_maxn
        for i in range(2, _maxn):
            fac[i] = fac[i-1] * i % mod
            inv[i] = _inv = (mod - inv[mod % i] * (mod // i) % mod) % mod
            facinv[i] = facinv[i-1] * _inv % mod
        self.fac = fac; self.facinv = facinv

    def nCr(self, n, r):
        """nCr
        n個のものからr個選ぶ
        """
        if ( r<0 or r>n ):
            return 0
        r = min(r, n-r)
        return self.fac[n] * (self.facinv[r] * self.facinv[n-r] % self.mod) % self.mod

cmb = Combination
ret = cmb.nCr(4, 2)


#####################################
# nは大きいが固定で,rは小さい場合
# nCr % 998244353  n～10^9 r～10^5
# nは大きいが固定で,rは小さい場合
#####################################
class CombinationSmallR:
    def __init__(self, n:int=10**9, mod:int=998244353) -> None:
        self.n = n
        self.max_r = 1
        self.mod = mod
        self.nCrseq = [1, n%mod]


    def __preprocessing(self, max_r:int) -> None:
        if max_r <= self.max_r: return
        mod, seq = self.mod, self.nCrseq
        seq += [0] * (max_r - self.max_r)
        for i in range(self.max_r + 1, max_r + 1):
            seq[i] = (seq[i-1] * (self.n-i+1) * pow(i,mod-2,mod)) % mod
        self.max_r = max_r


    def nCr(self, r:int) -> int:
        self.__preprocessing(r)
        return self.nCrseq[r]

cmb = CombinationSmallR(10)
print(cmb.nCr(4))



#####################################
# nCr % 3
#####################################
class CombinationMod3:
    def __init__(self, n=10**6):
        self.bf, self.bg = [0] * n, [0] * n
        self.bg[0] = 1

        for i in range(1, n):
            pos = i
            while pos % 3 == 0:
                pos //= 3; self.bf[i] += 1
            self.bg[i] = pos % 3

        for i in range(1, n):
            self.bf[i] += self.bf[i-1]
            self.bg[i] = self.bg[i] * self.bg[i-1] % 3
        self.MaxN = n

    def nCr(self, n, r):
        bf = self.bf
        if bf[n] != bf[r] + bf[n-r]: return 0
        bgn = self.bg[n]
        bgrnr = self.bg[r] * self.bg[n-r]
        if bgn == 1 and bgrnr == 1: return 1
        if bgn == 1 and bgrnr == 4: return 1
        if bgn == 2 and bgrnr == 2: return 1
        if bgn == 1 and bgrnr == 2: return 2
        if bgn == 2 and bgrnr == 1: return 2
        if bgn == 2 and bgrnr == 4: return 2
        return -1


c = CombinationMod3(10**6)
print(c.nCr(5,1))   #5mod3->2
print(c.nCr(5,2))   #10mod3->1
print(c.nCr(6,2))   #15mod3->0
print(c.nCr(6,3))   #20mod3->2

######prefix######
# Lib_N_nCr剰余
##############end##############
