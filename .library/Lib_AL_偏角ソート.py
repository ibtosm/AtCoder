######title######
# 偏角ソート
######subtitle######
# degree_sort(points): 偏角ソートした配列
# 原点<第一象限<第二象限<第三象限<第四象限

##############name##############
# 偏角ソート
######description######
# 偏角ソート
######body######
from functools import cmp_to_key
def degree_sort(points):
    def quadrant(x, y):
        if x == 0 and y == 0: return 0
        if x >= 0 and y >= 0: return 1
        if x <= 0 and y >= 0: return 2
        if x <= 0 and y <= 0: return 3
        if x >= 0 and y <= 0: return 4

    def points_cmp(p, q):
        p_qua = quadrant(*p)
        q_que = quadrant(*q)
        if p_qua == q_que:
            px, py = p
            qx, qy = q
            op = px * qy - py * qx
            return -1 if op > 0 else 1 if op < 0 else 0
        else:
            return -1 if p_qua < q_que else 1
    return sorted(points, key = cmp_to_key(points_cmp))
########################################
######prefix######
# Lib_AL_偏角ソート
##############end##############
