##############name##############
# BIT演算
######description######
# BIT演算
######body######


class Bit:
    def __init__(self, x: int = 0) -> None:
        self.x: int = int(x)

    def __bool__(self) -> bool:
        return self.x != 0

    def __int__(self) -> int:
        return self.x

    def __str__(self) -> str:
        return f"int: {self.x} bin: {self.bin()}"

    @property
    def len(self) -> int:
        return self.x.bit_length()

    @property
    def bitcount(self) -> int:
        return bin(self.x).count("1")

    def bin(self, l=32) -> str:
        return ("0" * l + bin(self.x)[2:])[-l:]

    def getkthbit(self, k) -> "Bit":
        """kビット目を取得"""
        return Bit(self.x & (1 << k))

    def isbitk(self, k) -> bool:
        return self.getkthbit(k).__bool__()

    def onkthbit(self, k) -> "Bit":
        """kビット目を１にした値"""
        return Bit(self.x | (1 << k))

    def offkthbit(self, k) -> "Bit":
        """kビット目を０にした値"""
        return Bit(self.x & ~(1 << k))

    def invertkthbit(self, k) -> "Bit":
        """kビット目を反転させた値"""
        return Bit(self.x ^ (1 << k))

    def invert(self) -> "Bit":
        """全ビット目を反転させた値"""
        return Bit(~self.x)

    def subset(self) -> list:
        """集合xの部分集合を列挙"""
        v = (-1) & self.x
        ret = []
        while v:
            ret.append(Bit(v))
            v = (v - 1) & self.x
        return ret

    def kcountsubset(self, k) -> list:
        """x以下の部分集合でビットがk個のものを列挙"""
        ret = []
        v = (1 << k) - 1
        while v < self.x:
            ret.append(Bit(v))
            x = v & -v
            y = v + x
            v = ((v & ~y) // x >> 1) | y
        return ret


x = Bit(7)
print(x)
print(x.onkthbit(0))
print(x.offkthbit(0))
print(x.invertkthbit(0))
print(x.invert())
print(x.isbitk(0))
print(x.isbitk(1))
print(x.isbitk(2))
print(x.isbitk(3))
print(x.isbitk(4))

for b in x.subset():
    print(b)
print("--")
for b in x.kcountsubset(2):
    print(b)


# https://qiita.com/qiita_kuru/items/3a6ab432ffb6ae506758

# 111
~((~0) << 3)  # 111
(1 << 3) - 1  # 111


######prefix######
# Lib_BIT演算
##############end##############
