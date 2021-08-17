from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        p = 0
        # 定义一个单调递减栈，用于存储凹陷处左边的高度，依次出栈，计算每个高度的所存的水
        stack = []
        res = 0

        while p < len(height):
            # 后面的判断条件保证栈是单调递减的，height[p]比栈顶大就要出栈计算，
            # 比栈顶小跳出循环，加入栈
            while len(stack) > 0 and height[p] > height[stack[-1]]:
                temp = stack.pop()
                # 如果为空，就没有左边界了
                if len(stack) == 0:
                    break
                # 计算高
                h = min(height[p], height[stack[-1]]) - height[temp]
                # 计算宽
                w = p - stack[-1] - 1
                res += h * w
            stack.append(p)
            p += 1
        return res


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))