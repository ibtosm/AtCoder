######title######
# 長方形探索
######subtitle######
# max_square(h, w, G, block):最大正方形
# max_rect(h, w, G, block):最大長方形
# left_min_position(A, min_value=0): 左で自分より小さいものがあるindexを高速で計算


##############name##############
# 長方形探索
######description######
# 長方形探索
######body######
#####################################
# 最大正方形
def max_square(h, w, G, block):
    dp = [[0] * w for _ in range(h)]
    mx = 0
    for i in range(h):
        if G[i][0] != block: dp[i][0] = 1; mx = 1
    for j in range(w):
        if G[0][j] != block: dp[0][j] = 1; mx = 1
    for i in range(1, h):
        for j in range(1, w):
            if G[i][j] == block: continue
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            mx = max(mx, dp[i][j])
    return mx

h, w = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(h)]
print(max_square(h, w, G, 1)**2)


#####################################
# 最大長方形面積
from collections import deque
def max_rect(h, w, G, block):
    height = [[0] * (w+1) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if G[i][j] == block: continue
            if i >= 1:
                height[i][j] = height[i-1][j] + 1
            else:
                height[i][j] = 1

    mx = 0
    for i, hist in enumerate(height):
        stack = deque([])
        for j, h in enumerate(hist):
            if not stack:
                stack.append((j, h))
            else:
                if stack[-1][1] < h:
                    stack.append((j, h))
                elif stack[-1][1] > h:
                    while stack and stack[-1][1] > h:
                        prev =stack.pop()
                        w2 = j - prev[0]
                        h2 = prev[1]
                        mx = max(mx, h2*w2)
                    stack.append((prev[0], h))
    return mx

h, w = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(h)]
print(max_rect(h, w, G, 1))

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
    return [n - pi - 1 for pi in reversed(left_min_position(A[::-1], min_value))]


n = int(input())
A = list(map(int, input().split()))
l = left_min_position(A)
r = right_min_position(A)

mx = 0
for li, ri, ai in zip(l, r, A):
    mx = max(mx, ai*(ri-li-1))
print(mx)

######prefix######
# Lib_A_長方形探索_最大正方形_最大長方形
##############end##############
