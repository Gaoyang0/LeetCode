from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)
        return -1

s = Solution()
print(s.findDuplicate([1,3,4,2,2]))