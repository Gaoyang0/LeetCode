from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        if len(temperatures) <= 1:
            return res

        # 栈顶最小
        stack_down = []
        for i in range(0, len(temperatures) - 1):
            if temperatures[i] < temperatures[i+1]:
                res[i] = 1
                while len(stack_down) > 0 and temperatures[i] > temperatures[stack_down[-1]]:
                    top = stack_down.pop()
                    res[top] = i - top
            else:
                while len(stack_down) > 0 and temperatures[i] > temperatures[stack_down[-1]]:
                    top = stack_down.pop()
                    res[top] = i - top
                stack_down.append(i)
        while len(stack_down) > 0:
            top = stack_down.pop()
            if temperatures[-1] > temperatures[top]:
                res[top] = len(temperatures) - 1 - top
        return res


s = Solution()
# print(s.dailyTemperatures([73, 73, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))


























# 栈
# res = [0] * len(temperatures)
# stack = []
#
# for i in range(len(temperatures) - 1):
#
#     while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
#         t = stack.pop(-1)
#         res[t] = i - t
#     if temperatures[i] < temperatures[i+1]:
#         res[i] = 1
#     else:
#         stack.append(i)
# while len(stack) > 0 and temperatures[-1] > temperatures[stack[-1]]:
#     t = stack.pop(-1)
#     res[t] = len(temperatures) - 1 - t
# return res
