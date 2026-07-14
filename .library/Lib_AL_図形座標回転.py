######title######
# 二次元の座標回転
######subtitle######
# rotate(point, R, isradian):

##############name##############
# Lib_AL_図形_座標回転
######description######
# 図形のライブラリ
######body######

########################
import math

########################
# 二次元座標を回転
########################
def rotate(point: tuple, R, isradian=True) -> tuple:
    if not isradian:
        R = math.radians(R)  # Rが度数の場合
    a, b = point
    cos, sin = math.cos(R), math.sin(R)
    return (cos*a-sin*b, sin*a+cos*b)


######prefix######
# Lib_AL_図形_座標回転
##############end##############
