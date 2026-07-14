##############name##############
# translate
######description######
# 複数の文字列を変換
######body######
s = '54IZSB'
ts:str= s.translate(str.maketrans("BSI","123"))
print(ts)
# 543Z21
######prefix######
# translate
# replace
##############end##############

##############name##############
# d進数
######description######
# nをd進数表記
######body######
##############################
# nをd進数表記
# d進数表記を10進数表記に
##############################

n = 32

print(format(n, 'b'))  # ２進数
print(format(n, 'o'))  # ８進数
print(format(n, 'x'))  # 16進数

print(bin(n))  # ２進数
print(oct(n))  # ８進数
print(hex(n))  # 16進数

# 任意のd進数
def base_repr(n:int, d:int) -> str:
    ret = ''
    while n != 0:
        n, r = divmod(n, d)
        ret += str(r)
    return ret[::-1]

print(base_repr(n, 2))
print(base_repr(n, 30))


##############################
# d進数表記を10進数表記に
##############################
s = '12'
d = 9
print(int(s, base=d))

# 関数版
def myint(s:str, d:int) -> int:
    ret = 0
    dig = 1
    for xi in s[::-1]:
        ret += int(xi)*dig
        dig *= d
    return ret

print(myint(s, 9))

######prefix######
# n進数
# d進数
##############end##############

##############name##############
# digital digit
######description######
#  -
# | |
#  -
# | |
#  -

######body######
led_statuses = ["1110111", "0100100", "1011101", "1101101", "0101110",
    "1101011", "1111011", "0100111", "1111111", "1101111"]
led_digit = [int(status, base=2) for status in led_statuses]
######prefix######
# digital digit
##############end##############
