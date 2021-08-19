from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        res = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            for index, f in enumerate(row):
                if f == "1":
                    heights[index] += 1
                else:
                    heights[index] = 0
            temp = self.largestRectangleArea(heights)
            res = max(res, temp)
        return res


    # 84题题解
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
# print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(s.maximalRectangle([["0","1"],["1","0"]]))