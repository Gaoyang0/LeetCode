# 判断一个正整数是不是2的整数次幂, 转为判断如果正整数 y 是 2 的整数次幂，
# 则 y 的二进制表示中只有最高位是 1，其余都是 0，因此 y&(y-1)=0
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        highBit = 0
        for i in range(1, n + 1):
            # 判断一个正整数是不是2的整数次幂, 转为判断如果正整数 y 是 2 的整数次幂，
            # 则 y 的二进制表示中只有最高位是 1，其余都是 0，因此 y&(y-1)=0
            if i & (i - 1) == 0:
                highBit = i
            # 将i拆分为i - highBit(bits[i - highBit])和highBit(1)
            # bits[i] = bits[i - highBit] + 1
            bits.append(bits[i - highBit] + 1)
        return bits
