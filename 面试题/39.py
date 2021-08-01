from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def back(cur, t, sub_candidates):
            if t < 0:
                return
            elif t == 0:
                res.append(cur.copy())
            else:
                for index, i in enumerate(sub_candidates):
                    cur.append(i)
                    # 去重复，剪枝
                    back(cur, t - i, sub_candidates[index:])
                    cur.pop(-1)

        back([], target, candidates)
        return res


s = Solution()

print(s.combinationSum([2,3,6,7], 7))

# a = []
# a = a.append("1")
# print(a)