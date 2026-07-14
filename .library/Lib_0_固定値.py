##############name##############
# modval1
######description######
# modval
######body######
mod = 1000000007
######prefix######
# mod = 1000000007
##############end##############

##############name##############
# modval2
######description######
# modval
######body######
mod = 998244353
######prefix######
# mod = 998244353
##############end##############

##############name##############
# pival
######description######
# pival
######body######
PI = 3.141592653589793
######prefix######
# pi_π円周率
##############end##############

##############name##############
# alphabet
######description######
# alphabet
######body######
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i, base='a')->str: return chr(ord(base) + i%26)    # i=0->'a', i=25->'z'
def alpind(a, base='a')->int: return ord(a)-ord(base)
######prefix######
# alphabet
##############end##############
