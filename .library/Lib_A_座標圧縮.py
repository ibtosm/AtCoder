######title######
# 座標圧縮
######subtitle######
# Compress: 座標圧縮して元の配列をID化
# Compress2D: 2次元版

##############name##############
# 座標圧縮
######description######
# 座標圧縮
######body######

from bisect import bisect_left
class Compress:
    """一次元座標圧縮

    Parameters
    ----------
    points : list
    値のリスト [100,300,50,900,200]

    Returns
    -------
    pos : {50: 0, 100: 1, 200: 2, 300: 3, 900: 4}
    vals : {0: 50, 1: 100, 2: 200, 3: 300, 4: 900}
    list : [1, 3, 0, 4, 2]
    """
    INF = 10**10
    def __init__(self, points, spacing=False, reverse=False):
        pos, vals, sx = {}, {}, set(points)
        if spacing: #スペースを作る場合
            for p in points: sx.add(p+1)
            sx.add(-self.INF)
            sx.add(self.INF)

        for i, xi in enumerate(sorted(set(sx), reverse=reverse)):
            pos[xi], vals[i] = i, xi
        self.pos, self.vals = pos, vals
        self.original_list, self.list = points, [pos[xi] for xi in points]
        self.valuesequence = sorted(self.pos.keys())

    def __contains__(self, original_value):
        return original_value in self.pos.keys()

    def index(self, original_value):
        """
        元の値 -> 圧縮後のインデックス/
        元の値がない場合は、None
        """
        if original_value in self:
            return bisect_left(self.valuesequence, original_value)
        return None

    def value(self, index):
        """
        圧縮後のインデックス -> 元の値/
        元の値がない場合は、None
        """
        if index in self.vals:
            return self.vals(index)
        return None

# c = Compress([100,300,50,900,200], spacing=True)

######prefix######
# Lib_A_座標圧縮_compress_zaatsu
##############end##############


##############name##############
# 座標圧縮二次元
######description######
# 座標圧縮二次元
######body######
from bisect import bisect_left
class Compress:
    INF = 10**10
    def __init__(self, points, spacing=False, reverse=False):
        pos, vals, sx = {}, {}, set(points)
        if spacing: #スペースを作る場合
            for p in points: sx.add(p+1)
            sx.add(-self.INF)
            sx.add(self.INF)

        for i, xi in enumerate(sorted(set(sx), reverse=reverse)):
            pos[xi], vals[i] = i, xi
        self.pos, self.vals = pos, vals
        self.original_list, self.list = points, [pos[xi] for xi in points]
        self.valuesequence = sorted(self.pos.keys())

    def __contains__(self, original_value):
        return original_value in self.pos.keys()

    def index(self, original_value):
        """
        元の値 -> 圧縮後のインデックス/
        元の値がない場合は、None
        """
        if original_value in self:
            return bisect_left(self.valuesequence, original_value)
        return None

    def value(self, index):
        """
        圧縮後のインデックス -> 元の値/
        元の値がない場合は、None
        """
        if index in self.vals:
            return self.vals(index)
        return None


class Compress2d:
    """二次元座標圧縮
    """
    def __init__(self, points, spacing=False):
        sx = [point[0] for point in points]
        sy = [point[1] for point in points]
        self.xc = Compress(sx, spacing=spacing)
        self.yc = Compress(sy, spacing=spacing)
        self.original_list = points
        self.list = list(zip(self.xc.list, self.yc.list))
        self.n = len(self.xc.valuesequence)
        self.m = len(self.yc.valuesequence)
        if len(points[0]) == 3:
            self.pointvalues = {self.index((x, y)): v for x, y, v in points}
        else:
            self.pointvalues = {self.index((x, y)): 0 for x, y in points}

    def index(self, original_point):
        """
        元の値 -> 圧縮後のインデックス/
        元の値がない場合は、None
        """
        x, y = original_point
        return self.xc.index(x), self.yc.index(y)

    def value(self, index_x, index_y):
        """
        圧縮後のインデックス -> 元の値/
        元の値がない場合は、None
        """
        return tuple(self.xc.value(index_x), self.yc.value(index_y))

    def xvalue(self, index):
        return self.xc.value(index)

    def yvalue(self, index):
        return self.yc.value(index)

# c = Compress2d([(1,1),(2,4),(5,3)], spacing=True)
# print(c.xc.valuesequence)
# print(c.yc.valuesequence)
# print(c.list)
######prefix######
# Lib_A_座標圧縮2D_compress_zaatsu
##############end##############
