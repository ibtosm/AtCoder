######title######
# 三角形
######subtitle######
# C(a, b, R): 二辺a,bと挟角Rから対辺の長さを計算
# S(a, b, R): 二辺a,bと挟角Rから面積を計算

##############name##############
# Lib_AL_図形_三角形_角度
######description######
# 図形のライブラリ
######body######

########################
import math

# 度→radian
math.radians(180)
# radian→度
math.degrees(3.1415)
########################
# 三角形
########################
# 余弦定理
# cosR = (a**2 + b**2 - c**2) / 2ab
# c**2 = a**2 + b**2 - 2*a*b*cosR
# 対辺
def C(a, b, R):
    """
    a, b: 二辺の長さ
    R: 角度
    Returns
    対辺の長さ
    """
    R = math.radians(R)  # Rが度数の場合
    return (a ** 2 + b** 2 - 2 * a * b * math.cos(R))**0.5

def S(a, b, R):
    """
    a, b: 二辺の長さ
    R: 角度
    Returns
    面積
    """
    R = math.radians(R)  # Rが度数の場合
    return abs(0.5 * a * b * math.sin(R))

######prefix######
# Lib_AL_図形_三角形_角度
##############end##############
