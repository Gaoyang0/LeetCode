from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1

        temp = heapq.nlargest(k, d.items(), key=lambda x:x[1])
        return [i[0] for i in temp]


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))