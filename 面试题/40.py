from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []

        res = set()
        def bak(cur, s, index):
            if s == target:
                if tuple(cur.copy()) not in res:
                    res.add(tuple(cur.copy()))
            if index == len(candidates):
                return
            elif s < target:
                for i in range(index, len(candidates)):
                    cur.append(candidates[i])
                    bak(cur, s + candidates[i], i + 1)
                    cur.pop()

        candidates.sort()
        bak([], 0, 0)
        return [list(i) for i in res]


s = Solution()
# print(s.combinationSum2([10,1,2,7,6,1,5], 8))
# print(s.combinationSum2([2,5,2,1,2], 5))
# print(s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27))
print(s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
, 30))
# print(len([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))