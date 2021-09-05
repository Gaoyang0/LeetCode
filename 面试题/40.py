from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        def bak(cur, s, index):
            if s == target:
                res.append(cur)
            elif s < target:
                for i in range(index, len(candidates)):
                    cur.append(candidates[i])
                    bak(cur, s + candidates[i], i + 1)
                    cur.pop()
        for index, item in enumerate(candidates):
            bak([item], item, index+1)
        return res


s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))