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
                    # break可以较少好多步骤
                    if s + candidates[i] > target:
                        break
                    # 和上一个重复
                    if i > index and candidates[i - 1] == candidates[i]:
                        continue
                    cur.append(candidates[i])
                    bak(cur, s + candidates[i], i + 1)
                    cur.pop()

        candidates.sort()
        bak([], 0, 0)
        return [list(i) for i in res]


s = Solution()
print(s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 30))