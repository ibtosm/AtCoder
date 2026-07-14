##############name##############
# Lib_math
######description######
# mathのライブラリ
######body######
import math
print(math.sin(math.pi/4))
print(math.cos(math.pi/4))
print(math.tan(math.pi/4))
# 度→radian
math.radians(180)
# radian→度
math.degrees(3.1415)

######prefix######
# Lib_math_最大公約数_三角関数
# import math
##############end##############

##############name##############
# Lib_decimal
######description######
# 四捨五入が正しくできるツール
# Decimal で扱う
######body######

pypyで使っちゃダメ！！！！！
from decimal import Decimal
x, y, r = map(Decimal, input().split())
f = 123.456
fd = Decimal(str(f))
fr = fd.quantize(Decimal('0'), rounding=ROUND_HALF_UP)  #123
fr = fd.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)#123.5
######prefix######
# Lib_四捨五入_Decimal
##############end##############

##############name##############
# Lib_math_複素数
######description######
# Lib_複素数
######body######
import cmath

z1 = 5 + 13j
a, b = 5, 13
z2 = complex(a, b)

print(z1.real)
print(z1.imag)


# 極座標表示
r, theta = cmath.polar(z1)

# 90度回転
print(cmath.rect(1, cmath.pi/2))
# (6.123233995736766e-17+1j)

# 共役数
print(z2.conjugate())
# (5-13j)

######prefix######
# Lib_math_複素数
##############end##############

##############name##############
# sort_by_function, OrderedObj
######description######
# sort_by_function, OrderedObj
######body######

# https://atcoder.jp/contests/abc308/tasks/abc308_c

class OrderedObj:
    def __init__(self, x):
        self.a, self.b, self.i = x

    def __lt__(self, other):
        # self < other 小さいを意味するときにTrueを返す
        if self.a * (other.a+other.b) < other.a * (self.a+self.b):
            return True
        if self.i > other.i:
            return True
        return False

    def __repr__(self):
        return f'{self.a} {self.b} {self.i}'


######prefix######
# Lib_sort_by_function比較
##############end##############


##############name##############
# Lib_sqroot
######description######
# Lib_sqroot
######body######
def sqrt(x):
    r = int(x**0.5) - 3
    while (r+1)*(r+1) <= x: r += 1
    return r
######prefix######
# Lib_sqroot
##############end##############
