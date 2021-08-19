from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调栈
        '''
        窗口在滑动的时候会删除一个数，加入一个数
        这个过程有个非常影藏且有用的规则：后加入窗口的数，会在是此刻窗口中最后一个被删除的数，
        因此，窗口中比加入的数小的数就没有用了（也就是不会成为后续窗口中的最大值）
        '''
        if len(nums) <= 1 or k <= 1:
            return nums

        diminishing_queue = [nums[0]]
        res = []
        for i in range(1, len(nums)):
            # nums[i]是要加入的， nums[i-k]是要删除的
            while len(diminishing_queue) > 0 and diminishing_queue[-1] < nums[i]:
                diminishing_queue.pop(-1)
            diminishing_queue.append(nums[i])

            if i >= k:
                if nums[i - k] == diminishing_queue[0]:
                    diminishing_queue.pop(0)
            if i >= k-1:
                res.append(diminishing_queue[0])
        return res

    # 大根堆


s = Solution()
# print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
# print(s.maxSlidingWindow([1], 1))
print(s.maxSlidingWindow([9, 11], 2))
# print(s.maxSlidingWindow([7,2,4], 2))
# print(s.maxSlidingWindow([8,7,9,2,4], 2))