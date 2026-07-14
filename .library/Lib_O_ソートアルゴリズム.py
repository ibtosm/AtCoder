######title######
# ソートアルゴリズム
######subtitle######
# BubbleSort
# SelectSort

##############name##############
# ソートアルゴリズム
######description######
# ソートアルゴリズム
######body######
def BubbleSort(A, N):
    # 後ろから大きいものを前にスワップしていく
    flag = True
    cnt = 0
    while flag:
        flag = False
        for i in range(1, N)[::-1]:
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                cnt += 1
                flag = True
    return A, cnt

def SelectionSort(A, N):
    # 前から最小値を見つけてスワップしていく
    cnt = 0
    for i in range(N):
        minpos = i
        for j in range(i+1, N):
            if A[j] < A[minpos]:
                minpos = j
        if i != minpos:
            A[i], A[minpos] = A[minpos], A[i]
            cnt += 1
    return A, cnt

n = int(input())
A = list(map(int, input().split()))

A, cnt = SelectionSort(A, n)
print(*A)
print(cnt)
######prefix######
# Lib_O_ソートアルゴリズム_Sort
##############end##############
