##############name##############
# print(ret)
######description######
# print(ret)
######body######
print(${1:ret})
######prefix######
# priret0
##############end##############

##############name##############
# print(INF⇒-1)
######description######
# print(INF⇒-1)
######body######
print(-1 if ${1:ret} == INF else ${1:ret})
######prefix######
# priret1
##############end##############

##############name##############
# YesNo
######description######
# YesNo
######body######
print('Yes' if ${1:ret} else 'No')
######prefix######
# priret2
##############end##############


##############name##############
# print('\n'.join(map, str(ret)))
######description######
# print('\n'.join(map, str(ret)))
######body######
print('\n'.join(map(str, ${1:ret})))
######prefix######
# priret3
##############end##############

##############name##############
# print("".join(ret))
######description######
# print("".join(ret))
######body######
print(''.join(${1:ret}))
######prefix######
# priret4
##############end##############

##############name##############
# rounded
######description######
# rounded10
######body######
def fstr(x):
    return f"{x:.10f}"
print(fstr(${1:ret}))

######prefix######
# priret5
##############end##############



##############name##############
# interactive i/o
######description######
# interactive
######body######
def req(${1:question}):
    print(f"? {${1:question}}", flush=True)
    return input()

def ans(${2:ret}):
    print(f"! {${2:ret}}", flush=True)
    return

######prefix######
# interactive
##############end##############
