# leetcode 167

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                return [p1+1, p2+1]
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
            else:
                p1 += 1

s = Solution()
print(s.twoSum(numbers = [2,7,11,15], target = 9))