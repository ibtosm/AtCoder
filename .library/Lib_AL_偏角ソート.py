######title######
# 偏角ソート
######subtitle######
# degree_sort(points): 偏角ソートした配列
# 原点<第一象限<第二象限<第三象限<第四象限

##############name##############
# 偏角ソート
######description######
# 偏角ソート
######body######
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Point:
    x: int
    y: int
    quadrant: int = field(init=False)

    def __post_init__(self) -> None:
        """quadrant"""
        if self.x >= 0 and self.y >= 0:
            self.quadrant = 1
        elif self.x <= 0 and self.y >= 0:
            self.quadrant = 2
        elif self.x <= 0 and self.y <= 0:
            self.quadrant = 3
        elif self.x >= 0 and self.y <= 0:
            self.quadrant = 4
        else:
            self.quadrant = 0

    def __str__(self) -> str:
        ret = f"({self.x}, {self.y}), "
        ret += f"quadrant: {self.quadrant}, "
        return ret

    def __lt__(self, other) -> Any | bool:
        if self.quadrant != other.quadrant:
            return self.quadrant < other.quadrant
        return self.ccw(other) > 0

    def ccw(self, other):
        # if p.ccw(q) > 0:
        #     # p -> q が反時計回り
        # if p.ccw(q) < 0:
        #     # 時計回り
        # if p.ccw(q) == 0:
        #     # 同一直線
        return self.x * other.y - self.y * other.x
########################################
######prefix######
# Lib_AL_偏角ソート
##############end##############
