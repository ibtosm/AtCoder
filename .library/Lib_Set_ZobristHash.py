######title######
# ゾブリストハッシュ
######subtitle######
# ZobristHash: 集合が一致しているか、数列が一致しているかがO(1)でわかる

##############name##############
# ゾブリストハッシュ
######description######
######body######
# https://atcoder.jp/contests/abc250/tasks/abc250_e -> Hash
# https://atcoder.jp/contests/abc367/tasks/abc367_f -> MultiHash

import random

class MultiHash:
    def __init__(self):
        self.mod = None
        self.hash = []

    def get(self, l, r):
        # returns hashvalue of [l, r)
        h = self.hash
        return (h[r] - h[l]) % self.mod

class Hash:
    def __init__(self):
        self.hash = []

    def get(self, l, r):
        # returns hashvalue of [l, r)
        h = self.hash
        return h[r] ^ h[l]

class ZobristHash:
    def __init__(self, elements: set|list, mod: int = (1<<61)-1):
        self.hash_table = {}
        self.mod = mod
        for e in elements:
            if e in self.hash_table: continue
            self.hash_table[e]= random.randint(1, mod)


    def create_MultiHash(self, X:list):
        hashstruct = MultiHash()
        hashX = [0]
        for x in X:
            hashX.append((hashX[-1] + self.hash_table[x]) % self.mod)
        hashstruct.mod = self.mod
        hashstruct.hash = hashX
        return hashstruct

    def create_Hash(self, X:list):
        hashstruct = Hash()
        hashX = [0]
        seen = set()
        for x in X:
            if x in seen:
                hashX.append(hashX[-1])
            else:
                hashX.append(hashX[-1] ^ self.hash_table[x])
            seen.add(x)
        hashstruct.hash = hashX
        return hashstruct

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

zob = ZobristHash(A+B)
hashA = zob.create_Hash(A)
hashB = zob.create_Hash(B)

Q = int(input())
for i in range(Q):
    x, y = map(int, input().split())
    print("Yes" if hashA.get(0, x) == hashB.get(0, y) else "No")


######prefix######
# Lib_Set_ZobristHash
##############end##############
