######title######
# 二つのソートされたリストの要素の差の最小値を探索
######subtitle######
# near(a, b):最小となる位置の組み合わせと値(i, j, a[i]-b[j])

##############name##############
# 差分最小値探索
######description######
# 差分最小値探索
######body######
def near(a:list, b:list) -> tuple:
    """二つのソートされたリストの要素の差の最小値を探索

    Returns
    -------
    tuple
        最小となる位置の組み合わせと値
        (i, j, a[i]-b[j])
    """
    INF = float('inf')
    if len(a) == 0 or len(b) == 0:
        return (None, None, INF)
    i, j = 0, 0
    retd = INF
    reta = -1
    retb = -1
    while i < len(a) and j < len(b):
        dist = abs(a[i] - b[j])
        if retd > dist:
            retd = dist
            reta= i
            retb = j
        if a[i] > b[j]:
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            break
    return (reta, retb, retd)
######prefix######
# Lib_A_差分最小値探索
##############end##############
