######title######
# ユニオンファインド
######subtitle######
# UnionFind(n)
# .find(x): xの親
# .unite(x, y, w): x と y の差を w として結合
# もし、不整合だったら"invalid"を返す
# .is_same(x, y): 同じグループかどうか
# .size(x): xが所属するグループの要素数を返す
# .get_groups(): リーダーに所属する要素一覧リストを返す

##############name##############
# ユニオンファインド
######description######
# ユニオンファインド
######body######

class UnionFind:
    """木の深さが小さい方を親にする"""
    def __init__(self, n):
        self.n = n                              # 要素数
        self.parents = [i for i in range(n)]    # 親
        self.ranks = [0] * n                    # 木の深さ
        self.sizes = [1] * n                    # グループの要素数
        self.groups = dict()                    # グループ key:parent, value:listofmember

    def find(self, x):
        if self.parents[x] == x: return x
        self.parents[x] = p = self.find(self.parents[x])
        return p

    def _choose_parent(self, x, y):
        """木の深さが大きい方を親とする"""
        if self.ranks[x] > self.ranks[y]:
            x, y = y, x
        if self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1
        return x, y

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        x, y = self._choose_parent(x, y)
        self.parents[x] = y
        self.sizes[y] += self.sizes[x]

    def is_same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x):
        """xのグループの要素数"""
        return self.sizes[self.find(x)]

    def get_groups(self):
        """親のリスト取得
            親ごとのグループのメンバー一覧取得
        """
        self.groups = dict()
        for i in range(self.n):
            p = self.find(i)
            if p not in self.groups:
                self.groups[p] = []
            self.groups[p].append(i)
        return

    def __str__(self):
        self.get_groups()
        print(f'group_count = {len(self.groups)}')
        return ' '.join([f'{p}:{v}' for p, v in sorted(self.groups.items())])

class UnionFindMax(UnionFind):
    def _choose_parent(self, x, y):
        """ノード番号が大きい方を親にする"""
        if x > y:
            x, y = y, x
        return x, y

class UnionFindMin(UnionFind):
    def _choose_parent(self, x, y):
        """ノード番号が小さい方を親にする"""
        if x < y:
            x, y = y, x
        return x, y


################

n, q = map(int, input().split())
uf = UnionFind(n)
for _ in range(q):
    p, a, b = map(int,input().split())
    # a -= 1; b -= 1
    if p == 0:
        uf.unite(a, b)
    else:
        if uf.is_same(a, b):
            print('Yes')
        else:
            print('No')

# https://atcoder.jp/contests/atc001/tasks/unionfind_a

######prefix######
# Lib_G_unionfind
##############end##############
