######title######
# 区間和の最大値
######subtitle######
# 区間和を累積和の差分としてその最大値を求めるar-al

##############name##############
# 区間和の最大値
######description######
# 区間和を累積和の差分としてその最大値を求めるar-al
######body######

class Imos:
    def __init__(self, a:list):
        self.origin = a
        self.accum = [0]
        for ai in a:
            self.accum.append(self.accum[-1] + ai)
        self.n = self.accum
        self.INF = float('inf')

    def _get_max(self, accum:list):
        """
        区間和(ar-al)の最大値
        max(ar-min(al))
        """
        ret_min = - self.INF
        min_al = self.INF
        for ar in accum:
            ret_min= max(ar - min_al, ret_min)
            min_al = min(ar, min_al)
        return ret_min

    @property
    def get_max(self):
        return self._get_max(self.accum)

    @property
    def get_min(self):
        return - self._get_max([-ai for ai in self.accum])


n = int(input())
a = list(map(int, input().split()))
for i, ai in enumerate(a):
    if ai==0:
        a[i] = -1

im = Imos(a)
print(im.get_max - im.get_min + 1)


######prefix######
# Lib_A_区間和の最大値
##############end##############
