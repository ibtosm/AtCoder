##############name##############
# ループ#
######description######
# ループ#
######body######
class Loop():
    """ループを検索して計算量圧縮

        Parameters
        ----------
        n : int
            鳩の巣の数
        x : int
            初期値
        f : function
            次の値を決める関数

        Notes
        ----------
        0->1->...->s_t-1 -> st->...-> s_t+x─┐
                             └─────────┘
        https://atcoder.jp/contests/typical90/tasks/typical90_bf

    """
    def __init__(self, n, x, f, g):
        self.hole = n
        self.ini_p = x
        self.nextp = f
        self.value = g
        self.__build()


    def __build(self):
        x = self.ini_p
        seen = defaultdict(int)
        seqs = []
        for i in range(self.hole + 10):
            seen[x] = i
            seqs.append(x)
            x = self.nextp(x)
            if x in seen: break
        p = seen[x]
        self.ini_seq = self.sequence([self.value(pos) for pos in seqs[:p]])
        self.lp_seq = self.sequence([self.value(pos) for pos in seqs[p:]])


    def get_kth(self, k:int)->int:
        """k番目の値を取得
        0-index
        """
        if k < self.ini_seq.len:
            return self.ini_seq.seq[k]
        else:
            k -= self.ini_seq.len
            _, k = divmod(k, self.lp_seq.len)
            return self.lp_seq.seq[k]


    def sum_kth(self, k:int)->int:
        """k番目までの値の累積和を取得
        0-index
        """
        if k < self.ini_seq.len:
            return self.ini_seq.acc[k]
        else:
            k -= self.ini_seq.len
            t, k = divmod(k, self.lp_seq.len)
            ret = self.ini_seq.acclast
            ret += self.lp_seq.acclast * t
            ret += self.lp_seq.acc[k]
            return ret


    class sequence:
        def __init__(self, seq):
            self.seq = seq          # 配列
            self.len = len(seq)     # 配列の個数
            self.acc = list(accumulate(seq))    # 配列の累積和
            if self.len == 0:
                self.acclast = 0    # 配列の累積和
            else:
                self.acclast = self.acc[-1]    # 配列の累積和


n, k = map(int, input().split())

if n == 0:
    print(0)
    exit()

def f(x):
    ...

def g(x):
    ...


lp = Loop(n, 0, f, g)
print(lp.get_kth(k))

######prefix######
# Lib_A_Loop_ループ
##############end##############
