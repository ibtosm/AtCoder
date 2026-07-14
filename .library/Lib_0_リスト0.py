##############name##############
# reverse=True
######description######
# ソートでのリバース
######body######
reverse=True
######prefix######
# reverse=True
##############end##############

##############name##############
# sort(key=itemgetter
######description######
# itemgetterソート
######body######
sort(key=lambda x: x[1])
######prefix######
# sort(key=lambda
##############end##############


##############name##############
# directions
######description######
# directions
######body######
directions4:list[tuple[int, int]]= [(1, 0), (0, 1), (-1, 0), (0, -1)]
directions8 :list[tuple[int, int]]= [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
directions_str:dict[str, tuple[int, int]] = {"R":(1, 0), "U":(0, 1), "L":(-1, 0), "D":(0, -1)}

def move(cur:tuple|list, d:tuple|list) -> None|tuple:
    H:int = H
    W:int = W
    next0:int = cur[0] + d[0]
    next1:int = cur[1] + d[1]

    if (0 <= next0 < H) and (0 <= next1 < W):
        return (next0, next1)
    return None

######prefix######
# directions
##############end##############
