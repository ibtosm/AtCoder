##############name##############
# Lib_G_枝刈り取る
######description######
# グラフの葉から枝を刈り取って、ループ部分のみ抽出する
######body######

def cycle(n, G):
    degree = [0] * n
    for gi in G:
        for i in gi:
            degree[i] += 1

    leaves = [i for i in range(n) if degree[i] == 1]
    oncycle = set(range(n))
    while leaves:
        x = leaves.pop()
        oncycle.remove(x)
        for y in G[x]:
            degree[y] -= 1
            if degree[y] == 1:
                leaves.append(y)
    return oncycle


n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

print(cycle(n, G))

######prefix######
# Lib_G_cycle
##############end##############
