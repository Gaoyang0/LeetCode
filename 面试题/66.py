from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 初始+1
        sign = 1
        for i in range(len(digits) - 1, -1, -1):
            tmp = digits[i] + sign
            # 当+=1后小于10，终止循环
            if tmp < 10:
                digits[i] = tmp
                sign = 0
                break
            else:
                # 将i赋值为0
                digits[i] = 0
        # 当[9]这种情况时，需要考虑sign是否为1，向列表头插入1
        if sign:
            digits.insert(0, 1)
        return digits

s = Solution()
print(s.plusOne([1, 2]))