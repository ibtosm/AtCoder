##############name##############
# output0
######description######
# print(ret)
######body######
print($ret)
######prefix######
# print(0ret)
##############end##############

##############name##############
# output2
######description######
# print(INF⇒-1)
######body######
print(-1 if $ret == INF else $ret)
######prefix######
# print(2INF⇒-1)
##############end##############

##############name##############
# output3
######description######
# print(3'\n'.join(map)
######body######
print('\n'.join(map(str, $ret)))
######prefix######
# print(3'\n'.join(map(str)
##############end##############

##############name##############
# output4
######description######
# print("".join)
######body######
print(''.join($ret))
######prefix######
# print(4''.join(ret))
##############end##############


##############name##############
# output interactive
######description######
# interactive
######body######
def req($ret): print($ret, flush=True)

######prefix######
# print(6interactive)
##############end##############

##############name##############
# output7
######description######
# rounded
######body######
def fstr(x): return f'{x:.10f}'

######prefix######
# print(7roundeds)
##############end##############

##############name##############
# outputYesNo
######description######
# outputYesNo
######body######
print('Yes' if $ret else 'No')
######prefix######
# print(5yesno)
##############end##############
