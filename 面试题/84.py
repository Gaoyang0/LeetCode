from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        # 单调递增栈
        increasing_stack = [0]
        p = 1
        while p < len(heights):
            while len(increasing_stack) > 0 and heights[increasing_stack[-1]] > heights[p]:
                # 以heights[temp]为高度的最大面积可以计算了
                temp = increasing_stack.pop()
                left = -1 if len(increasing_stack) == 0 else increasing_stack[-1]
                w = p - left - 1
                res = max(heights[temp]*w, res)
            increasing_stack.append(p)
            p += 1

        while len(increasing_stack) > 0:
            temp = increasing_stack.pop()
            left = -1 if len(increasing_stack) == 0 else increasing_stack[-1]
            w = len(heights) - left - 1
            res = max(heights[temp] * w, res)
        return res


s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))