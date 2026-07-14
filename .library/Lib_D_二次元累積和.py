######title######
# 二次元累積和
######subtitle######
# Imos:クラス

##############name##############
# 累積和
######description######
# 累積和
######body######
class Imos:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        # 拡張grid生成
        self.grid = [[0] * (w+1) for _ in range(h+1)]

    def import_grid(self, grid):
        for i in range(self.h):
            for j in range(self.w):
                self.grid_add(i, j, grid[i][j])

    def grid_add(self, i, j, value):
        # i, j is 0 index on original_grid
        self.grid[i+1][j+1] += value

    def accumlate(self):
        # 累積和
        for i in range(self.h+1):
            for j in range(1, self.w+1):
                self.grid[i][j] += self.grid[i][j-1]
        for j in range(self.w+1):
            for i in range(1, self.h+1):
                self.grid[i][j] += self.grid[i-1][j]

    def sum(self, x, y, u, v):
        # x <= i < u, y <= j < v　の範囲をカウント
        if not 0<= x <= u < self.h+1: return 0
        if not 0<= y <= v < self.w+1: return 0
        gd = self.grid
        return gd[u][v] - gd[u][y] - gd[x][v] + gd[x][y]

###############################################
h, w, n = map(int, input().split())
im = Imos(h, w)
for _ in range(n):
    a, b, c, d = map(int, input().split())
    im.grid_add(a-1, b-1, 1)
    im.grid_add(c, d, 1)
    im.grid_add(a-1, d, -1)
    im.grid_add(c, b-1, -1)

im.accumlate()
for i in range(im.h):
    print(*im.grid[i][:-1])

######prefix######
# Lib_D_累積和_accum
##############end##############
