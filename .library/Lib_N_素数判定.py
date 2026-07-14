######title######
# 素数判定・出力

######subtitle######
# is_prime(n):素数判定 O(n**0.5)
# miller_rabin(n):素数ミラーラビン判定 n < 10**18, Q = 10**5回
# get_prime(n):n以下の素数出力 O(n**0.5)
# count_primes(n):n以下の素数の数 O(n**0.5)


##############name##############
# 素数判定・出力
#descripiton#
# 素数判定・出力
######body######

##############################
# 素数判定 O(n**0.5)
##############################
def is_prime(n:int) -> bool:
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True

#####################
print(10, is_prime(10))
print(31, is_prime(31))
#####################


##############################
# 素数ミラーラビン判定
# N < 10**18, Q = 10**5回
##############################

from random import randint as ri

def miller_rabin(N, Times=10):
    if N == 2: return True
    if N == 1 or N%2 == 0: return False

    q = N-1
    k = 0
    while q&1==0:
        q >>= 1
        k += 1

    for _ in range(Times):
        m = ri(2, N-1)
        y = pow(m, q, N)
        if y == 1: continue

        for _ in range(k):
            if (y+1) % N == 0: break
            y = y * y % N

        else: return False
    return True


for _ in range(int(input())):
    n = int(input())
    print('Yes' if miller_rabin(n, 10) else 'No')


##############################
# 素数出力 O(n**0.5)
# n <= 10**5
##############################
def get_primes(n:int) -> list:
# n以下の素数列挙
    isPrime = [False, False, True, True] + [False, True] * ((n - 4) // 2)
    primes = [2]
    for p in range(3, n, 2):
        if isPrime[p]:
           primes.append(p)
           for q in range(p * p, n, p):
               isPrime[q] = False
    return primes


##############################
# 素数出力 O(n**0.5)
# 区間篩
# L = 10**14
# R - L <= 10**5
##############################
def get_primes_segments(L:int , R:int) -> list:
    # √R 以下の素数を炙り出すための篩
    sqrtR = int(R**0.5)
    isPrime = [True] * (sqrtR + 1)
    isPrime2 = [True] * (R - L + 1)
    primes = []
    # ふるい
    for p in range(2, sqrtR + 1):
        # すでに合成数であるものはスキップする
        if not isPrime[p]: continue
        # p 以外の p の倍数から素数ラベルを剥奪
        q = p * 2
        while q * q <= R:
            isPrime[q] = False
            q += p
        # L 以上の最小の p の倍数
        start = L + (-L) % p
        if start == p:
            start = p * 2
        # L 以上 R 以下の整数のうち、p の倍数をふるう
        q = start
        while q <= R:
            isPrime2[q - L] = False
            q += p
    primes = [p + L for p, v in enumerate(isPrime2) if v]
    return primes


##############################
# n以下の素数の数 O(n**0.5)
# n ～ 10**12 for pypy3
##############################
def count_primes(n:int):
    if n < 2:
        return 0
    v = int(n ** 0.5) + 1
    smalls = [i // 2 for i in range(1, v + 1)]
    smalls[1] = 0
    s = v // 2
    roughs = [2 * i + 1 for i in range(s)]
    larges = [(n // (2 * i + 1) + 1) // 2 for i in range(s)]
    skip = [False] * v

    pc = 0
    for p in range(3, v):
        if smalls[p] <= smalls[p - 1]:
            continue

        q = p * p
        pc += 1
        if q * q > n:
            break
        skip[p] = True
        for i in range(q, v, 2 * p):
            skip[i] = True

        ns = 0
        for k in range(s):
            i = roughs[k]
            if skip[i]:
                continue
            d = i * p
            larges[ns] = larges[k] - \
                (larges[smalls[d] - pc] if d < v else smalls[n // d]) + pc
            roughs[ns] = i
            ns += 1
        s = ns
        for j in range((v - 1) // p, p - 1, -1):
            c = smalls[j] - pc
            e = min((j + 1) * p, v)
            for i in range(j * p, e):
                smalls[i] -= c

    for k in range(1, s):
        m = n // roughs[k]
        s = larges[k] - (pc + k - 1)
        for l in range(1, k):
            p = roughs[l]
            if p * p > m:
                break
            s -= smalls[m // p] - (pc + l - 1)
        larges[0] -= s

    return larges[0]


##############################
# n!が素数pで何回割れるか O(logn)
# legendre(n, p)
##############################
def legendre(n, p):
    ret = 0
    while n > 0:
        ret += n // p
        n //= p
    return ret

######prefix######
# Lib_N_prime_素数
##############end##############
