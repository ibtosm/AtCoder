######title######
# 二次元点クエリ
######subtitle######
# RangeSearchQuery(A): ポイントのリストAを与えてクラスをインスタンス
# query(sx, tx, sy, ty): 二次元点のリストで範囲を指定して、含まれる要素番号を出力する

##############name##############
# 二次元点クエリ
######description######
# 二次元点クエリ
######body######
from bisect import bisect_left, bisect_right

class RangeSearchQuery:
    """
    二次元点のリストで範囲を指定して、含まれる要素番号を出力する
    ２次元の平面上の点の集合に対し、与えられた領域に含まれる点を列挙してください。
    ただし、与えられた点の集合に対して、点の追加・削除は行われません。
    """
    def __init__(self, points):
        self.n = len(points)
        self.p_id = {v: i for i, v in enumerate(points)}  #座圧
        data = dict()
        for x, y in points:
            if x not in data: data[x] = []
            data[x].append(y)
        self.d_x = sorted(list(data.keys()))
        for dv in data.values(): dv.sort()
        self.data = data

    def query(self, sx, tx, sy, ty):
        ans = []
        left = bisect_left(self.d_x, sx)
        right = bisect_right(self.d_x, tx)
        for kx in self.d_x[left:right]:
            y_left = bisect_left(self.data[kx], sy)
            y_right = bisect_right(self.data[kx], ty)
            for ky in self.data[kx][y_left: y_right]:
                ans.append(self.p_id[(kx, ky)])
        return ans

n = int(input())
A = [tuple(map(int, input().split())) for _ in range(n)]
RSQ = RangeSearchQuery(A)

q = int(input())
for _ in range(q):
    que = tuple(map(int, input().split()))
    ans = RSQ.query(*que)
    for ans_i in sorted(ans):
        print(ans_i)
    print()


######prefix######
# compress_zaatsu
# Lib_A_二次元点クエリ
##############end##############
