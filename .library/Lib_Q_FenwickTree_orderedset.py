##############name##############
# Ordered set (BIT)
######description######
######body######

class BinaryIndexedTree:
    # 初期化処理
    def __init__(self, size):
        self.size = size
        self.dat = [0]*(size+1)
        self.depth = size.bit_length()

    def init(self, a):
        for i, x in enumerate(a):
            self.add(i, x)

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.dat[i] += x
            i += i & -i # 更新すべき位置

    def update(self, i, x):
        x -= self[i]
        self.add(i, x)

    def sum(self, r):
        """
        Returns
        -------
        sum of [0, r]
        """
        r += 1
        ret = 0
        while r>0:
            ret += self.dat[r]
            r -= r & -r # 加算すべき位置
        return ret

    def range_sum(self, l, r):
        """閉区間 [l,r] の合計を取得する

        Returns
        -------
        sum of [l, r]
        """
        if l == 0:
            return self.sum(r)
        else:
            return self.sum(r) - self.sum(l-1)


    def __getitem__(self, i):
        return self.range_sum(i, i)


    def right_bound_of_x(self, x):
        # pos       : sum([0, pos]) < x     となる最大のindex
        sum_, pos = 0, 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.dat[k] <= x:
                sum_ += self.dat[k]
                pos += 1 << i
        return pos

    def right_bound_include_x(self, x):
        # pos       : sum([0, pos]) <= x     となる最大のindex
        sum_, pos = 0, 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.dat[k] < x:
                sum_ += self.dat[k]
                pos += 1 << i
        return pos

    def left_bound_of_x(self, x):
        # pos   : x < sum([0, pos])  となる最小のindex
        return self.right_bound_include_x(x) - 1

    def left_bound_include_x(self, x):
        # pos   : x <= sum([0, pos])  となる最小のindex
        return self.right_bound_of_x(x) - 1

########################################
class OrderedSet:
    """
        init の時に取りえる値を固定
        __contains__: v in XXX
        __len__: len(XXX)
        add(v):
        discard(v):
        index(v): 値vの最初のインデックス(0-index)
        kthvalue(k): 0-indexでのk番目の値
    """
    def __init__(self, vals):
        vals = sorted(set(vals))
        INF = max(abs(min(vals)), abs(max(vals)), 10**9)
        INF = pow(10, len(str(INF))+1)
        self.LINF = - INF
        self.RINF = INF
        self.vals = [self.LINF] + vals + [self.RINF]
        self.valtoid = {v: i for i, v in enumerate(self.vals)}
        self.BIT = BinaryIndexedTree(len(self.vals))
        self.size = 0

    def __contains__(self, v):
        if not v in self.valtoid: return False
        return self.BIT[self.valtoid[v]] >= 1

    def __len__(self):
        return self.size

    def add(self, v):
        if v in self.valtoid and not v in self:
            self.size += 1
            self.BIT.update(self.valtoid[v], 1)
            return True
        else:
            return False

    def discard(self, v):
        if v in self:
            self.BIT.add(self.valtoid[v], -1)
            self.size -= 1
            return True
        else:
            return False

    def count(self, v):
        if v not in self.valtoid: return -1
        return self.BIT[self.valtoid[v]]

    def index(self, v):
        if v not in self.valtoid: return -1
        return self.BIT.sum(self.valtoid[v]-1)

    def left_index(self, v):
        return self.index(v)

    def right_index(self, v):
        if v not in self.valtoid: return -1
        return self.index(v) + self.count(v)

    def kth_value(self, k):
        pos = self.BIT.right_bound_of_x(k)
        return self.vals[pos]

    def prev_value(self, v):
        k = self.left_index(v) - 1
        return self.kth_value(k)

    def next_value_include_self(self, v):
        "v以上の値"
        if self.count(v) > 0: return v
        return self.next_value(v)

    def next_value(self, v):
        "vより大きい値"
        k = self.right_index(v)
        if k == self.size: return self.RINF
        return self.kth_value(k)

    def __str__(self):
        isfirst = True
        ret = "{"
        for v in self.vals:
            if not v in self: continue
            ret += f"{v}: {self.count(v)}" if isfirst else f", {v}: {self.count(v)}"
            isfirst = False
        ret += "}"
        return ret


########################################
class OrderedMultiSet(OrderedSet):
    """
        count(v): vの個数
        left_index(v): 値vの最初のインデックス(0-index)
        right_index(v): 値vの次の値の最初のインデックス(0-index)
    """
    def __init__(self, vals):
        super().__init__(vals)

    def add(self, v):
        if v in self.valtoid:
            self.BIT.add(self.valtoid[v], 1)
            self.size +=1
            return True
        else:
            return False


##################################################
A = [1,2,3,100,100100100,100100, 200200200]
os = OrderedMultiSet(A)
#os = OrderedSet(A)

os.add(3)
os.add(100)
os.add(100)
os.add(100100100)
# os.add(100100)
# os.add(100100)
print(os.vals)
print(os)

for i in range(len(os)):
    print(os.kth_value(i))

for ai in A:
    x = os.index(ai)
    y = os.left_index(ai)
    z = os.right_index(ai)
    pv = os.prev_value(ai)
    nv = os.next_value(ai)
    niv = os.next_value_include_self(ai)
    print(ai, y, z, pv, nv, niv)


#print(os.kthvalue(0))
######prefix######
# Lib_D_OrderedSet_BIT
##############end##############
