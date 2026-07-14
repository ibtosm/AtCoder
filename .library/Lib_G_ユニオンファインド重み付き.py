######title######
# ユニオンファインド重み付き（ポテンシャル）

######subtitle######
# UnionFindWeighted(n)
# .find(x): xの親
# .unite(x, y, w): x と y の差を w として結合
# もし、不整合だったら"invalid"を返す
# .weight(x): xの重み
# .diff(x, y): x と y の重みの差
# .is_same(x, y): 同じグループかどうか
# .get_groups(): リーダーに所属する要素一覧リストを返す
# self.leadersはリーダーの集合も作成

##############name##############
# ユニオンファインド重み付き
######description######
# ユニオンファインド重み付き
######body######

class UnionFindWeighted:
    def __init__(self, n):                      # 初期化
        self.INF = 1e18
        self.n = n                              # 要素数
        self.parents = [i for i in range(n)]    # 親
        self.ranks = [0] * n                    # 木の深さ
        self.sizes = [1] * n                    # グループの要素数
        self.weights = [0] * n                  # 親との重み
        self.isvalid = [True] * n               # ポテンシャルがプラスの閉路あり
        self.leaders = None                     # リーダー
        self.groups = None                      # グループ

    def find(self, x):
        if self.parents[x] == x: return x
        p = self.find(self.parents[x])
        self.weights[x] += self.weights[self.parents[x]]
        self.parents[x] = p
        return p

    def unite(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            if self.diff(x, y) != w:
                self.isvalid[rx] = False
                return "invalid"    # 整合性がない情報がある
            else:
                return "pass"       # 整合性がある
        # a[x]->a[y]  の差はw  # a[y] = a[x] + w
        wx = self.weight(x)
        wy = self.weight(y)
        if self.ranks[rx] > self.ranks[ry]:
            rx , ry = ry, rx    #ryを親にする
            wx , wy = wy, wx
            w *= -1
        elif self.ranks[rx]==self.ranks[ry]:
            self.ranks[ry] += 1
        self.parents[rx] = ry
        self.sizes[ry] += self.sizes[rx]
        self.weights[rx] = wy - wx - w
        self.isvalid[ry] &= self.isvalid[rx]
        return "unite"

    def is_same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def get_size(self, x):
        """xのグループの要素数"""
        return self.sizes[self.find(x)]

    def get_groups(self):
        """親のリスト取得
            親ごとのグループのメンバー一覧取得
        """
        leader_buf = [self.find(i) for i in range(self.n)]
        self.leaders = []
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            if leader_buf[i] == i:
                self.leaders.append(i)
            result[leader_buf[i]].append(i)
        self.gropus = result
        return result

    def weight(self, x):
        """重み"""
        self.find(x)
        return self.weights[x]

    def diff(self, x, y):
        """重みの差"""
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry: return self.INF
        return self.weight(y) - self.weight(x)

    def __str__(self):
        return '\n'.join(f'{r}: {self.members(r)}' for r in self.leaders)

################

n, m = map(int, input().split())
uf = UnionFindWeighted(n)
for _ in range(m):
    a, b, w = map(int,input().split())
    a -= 1; b -= 1
    uf.unite(a, b, w)

######prefix######
# Lib_G_unionfind_weighted
##############end##############
