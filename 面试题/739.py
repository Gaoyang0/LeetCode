from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 栈
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1):

            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                t = stack.pop(-1)
                res[t] = i - t
            if temperatures[i] < temperatures[i+1]:
                res[i] = 1
            else:
                stack.append(i)
        while len(stack) > 0 and temperatures[-1] > temperatures[stack[-1]]:
            t = stack.pop(-1)
            res[t] = len(temperatures) - 1 - t
        return res



s = Solution()
print(s.dailyTemperatures([30,40,40,60]))

