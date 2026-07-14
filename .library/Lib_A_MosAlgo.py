######title######
# Mo アルゴリズム
######subtitle######
# A:リスト n = 10**5
# Q: l, r, q = 10**5
# O(NQ−−√)が間に合う条件である*3
# 区間伸縮の計算がO(1) またはそれに近い
# クエリがオフラインで与えられる(先読みができる)
# 配列の要素が不変である

##############name##############
# Mo'sAlgorithm#
######description######
# Mo'sAlgorithm#
######body######

class _Mo:
    def __init__(self, N:int, Q:int):
        self.N=N
        self.Q = Q
        self.shift = 20
        self.M = int(Q**0.5)+1  # bucket num
        self.data = [0] * Q
        self.query = [[] for _ in range(self.M)]

    def add_query(self, l:int, r:int, i:int):
        """
        半開区間 [l,r)
        """
        sft=self.shift
        h=l*self.M//self.N
        self.data[i]=(l<<sft)|r
        self.query[h].append(((r if h&1 else -r)<<sft)+i)
    def solve(self):
        mask=(1<<self.shift)-1
        assert max(self.N, self.Q)<=mask
        L=R=0
        ret = [0]*self.Q
        for bucket in self.query:
            bucket.sort()
            for lri in bucket:
                i = lri&mask
                l,r=divmod(self.data[i],1<<self.shift)
                while L>l:
                    L-=1
                    self.add_left(L)
                while R<r:
                    self.add_right(R)
                    R+=1
                while L<l:
                    self.remove_left(L)
                    L+=1
                while R>r:
                    R-=1
                    self.remove_right(R)
                ret[i] = self.get_state()
        return ret

N,Q=map(int,input().split())
# N=int(input())
A=list(map(int,input().split()))

class Mo(_Mo):
    def __init__(self, N, Q):
        super().__init__(N, Q)
        self.value = 0
        self.count = [0] * (max(A)+1)
    def get_state(self):
        return self.value
    # https://atcoder.jp/contests/abc293/tasks/abc293_g
    def add_left(self, i):
        a = A[i]
        x = self.count[a]
        self.count[a] += 1
        self.value += x*(x-1) // 2
    def remove_left(self, i):
        a = A[i]
        x = self.count[a]
        self.count[a] -= 1
        self.value -= (x-1)*(x-2)//2

    # https://atcoder.jp/contests/abc174/tasks/abc174_f
    # def add_left(self, i):
    #     a = A[i]
    #     if a in self.count:
    #         self.count[a] += 1
    #     else:
    #         self.count[a] = 1
    #     if self.count[a] == 1:
    #         self.value += 1
    # def remove_left(self, i):
    #     a = A[i]
    #     self.count[a] -= 1
    #     if self.count[a] == 0:
    #         self.value -= 1

# https://atcoder.jp/contests/abc242/tasks/abc242_g
    # def add_left(self, i):
    #     a = A[i]
    #     x = self.count[a]
    #     self.count[a] += 1
    #     self.value += (x+1) // 2 - x // 2
    # def remove_left(self, i):
    #     a = A[i]
    #     x = self.count[a]
    #     self.count[a] -= 1
    #     self.value -= x // 2 - (x-1) // 2

    add_right = add_left
    remove_right = remove_left


mo = Mo(N, Q)
# Q=int(input())
for i in range(Q):
    l,r=map(int,input().split())
    mo.add_query(l-1,r, i)
ans = mo.solve()

print("\n".join(map(str,ans)))


######prefix######
# Lib_Mos_モアルゴリズム
##############end##############
