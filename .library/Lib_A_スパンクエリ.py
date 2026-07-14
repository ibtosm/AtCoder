######title######
# スパンクエリ

######subtitle######
# left_min_positon(A, v):左で自分より小さいものがあるindexを高速で計算
# right_min_positon(A, v):右で自分より小さいものがあるindexを高速で計算

##############name##############
# スパンクエリ
######description######
# スパンクエリ
######body######
#####################################
# 左で自分より小さいものがあるindexを高速で計算
def left_min_position(A, min_value=0):
    ret = []
    stack = []
    stack.append([min_value, -1])
    for i, ai in enumerate(A):
        while stack[-1][0] >= ai:   #
            stack.pop()
        ret.append(stack[-1][1])
        stack.append([ai, i])
    return ret

def right_min_position(A, min_value=0):
# 右で自分より小さいものがあるindexを高速で計算
    n = len(A)
    return [n - pi - 1 for pi in reversed(left_min_position(A[::-1]))]


n = int(input())
A = list(map(int, input().split()))
l = left_min_position(A)
r = right_min_position(A)

mx = 0
for li, ri, ai in zip(l, r, A):
    mx = max(mx, ai*(ri-li-1))
print(mx)

######prefix######
# Lib_A_スパンクエリ_left_min_position
##############end##############
