######title######
# 行列回転
######subtitle######
# rotate: tだけシフト回転
# reverse_lr: 左右反転
# reverse_ud: 上下反転


##############name##############
# 行列演算2
#descripiton#
# 行列回転
######body######
class Matrix():
    def __init__(self, n, v=None):
        self.n = n
        self.state = [0, 0]
        self.matrix_origin = [[v] * n for _ in range(n)]

    def rotate(self, t):
        self.state[0] = (self.state[0] + t) % 4


    def reverse_lr(self):
        self.state[1] = 1 - self.state[1]
        if self.state[0] % 2 == 1:
            self.state[0] = (self.state[0] + 2) % 4

    def reverse_ud(self):
        self.state[1] = 1 - self.state[1]
        if self.state[0] % 2 == 0:
            self.state[0] = (self.state[0] + 2) % 4

    def get_original_positon(self, x, y):
        n = self.n
        if self.state == [0, 0]: return x, y
        if self.state == [1, 0]: return n-1-y, x
        if self.state == [2, 0]: return n-1-x, n-1-y
        if self.state == [3, 0]: return y, n-1-x

        if self.state == [0, 1]: return x, n-1-y
        if self.state == [1, 1]: return n-1-y, n-1-x
        if self.state == [2, 1]: return n-1-x, y
        if self.state == [3, 1]: return y, x
        else:
            print(self.state)

    def set_value(self, x, y, v):
        ox, oy = self.get_original_positon(x, y)
        self.matrix_origin[ox][oy] = v

    def get_value(self, x, y):
        ox, oy = self.get_original_positon(x, y)
        return self.matrix_origin[ox][oy]

n, q = map(int, input().split())
mx = Matrix(n, 0)

for _ in range(q):
    que = list(input().split())
    if que[0] == '1':
        x = int1(que[1])
        y = int1(que[2])
        mx.set_value(x, y, 1 - mx.get_value(x, y))
    if que[0] == '2':
        if que[1] == 'A':
            mx.rotate(1)
        else:
            mx.rotate(3)
    if que[0] == '3':
        if que[1] == 'A':
            mx.reverse_ud()
        else:
            mx.reverse_lr()

for i in range(n):
    ret = []
    for j in range(n):
        ret.append(mx.get_value(i, j))
    print(''.join(map(str, ret)))

######prefix######
# Lib_M_matrix-回転と反転
##############end##############
