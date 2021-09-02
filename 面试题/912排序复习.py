import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 归并
        # 堆
        # 快速
        # 桶
        # self.heap_sort(nums)
        random.shuffle(nums)
        self.quick_sort(nums, 0, len(nums)-1)
        return nums

    def quick_sort(self, arr, start, end):
        """快速排序"""
        # 递归的退出条件
        if start >= end:
            return

        select = random.randint(start, end)
        arr[start], arr[select] = arr[select], arr[start]

        mid = arr[start]
        low = start
        high = end

        while low < high:
            # 从右往左，找到第一个比mid小的
            while low < high and arr[high] >= mid:
                high -= 1
            # 放在low的位置上
            arr[low] = arr[high]
            # 从左往右，找到第一个比mid大的
            while low < high and arr[low] < mid:
                low += 1
            # 放在high的位置上
            arr[high] = arr[low]
        arr[low] = mid
        self.quick_sort(arr, start, low - 1)
        self.quick_sort(arr, low + 1, end)


    def heap_sort(self, nums):
        def adjust_down(arr, root, length):
            lc = root * 2 + 1
            rc = root * 2 + 2

            larger = root
            if lc < length and arr[lc] > arr[larger]:
                larger = lc
            if rc < length and arr[rc] > arr[larger]:
                larger = rc
            if root != larger:
                arr[larger], arr[root] = arr[root], arr[larger]
                adjust_down(arr, larger, length)

        def build_heap(arr):
            for i in range((len(arr) - 1) // 2, -1, -1):
                adjust_down(arr, i, len(arr))

        build_heap(nums)
        for i in range(len(nums), 0, -1):
            adjust_down(nums, 0, i)
            nums[0], nums[i-1] = nums[i-1], nums[0]



s = Solution()
print(s.sortArray([5,1,1,2,0,0]))
