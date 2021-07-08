# from typing import List
#
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         if len(intervals) == 0:
#             return [newInterval]
#
#         def binary_search(nums, target):
#             low = 0
#             high = len(nums) - 1
#             while low <= high:
#                 mid = (low + high) // 2
#
#                 if nums[mid] == target:
#                     return mid
#                 if nums[mid] > target:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             return low
#
#         index = binary_search([i[0] for i in intervals], newInterval[0])
#         intervals.insert(index, newInterval)
#         print(index)
#         print(intervals)
#
#         if index == 0:
#             res = [intervals[0]]
#             index = 1
#         else:
#             res = []
#             res.extend(intervals[:index])
#
#         for i in range(index, len(intervals)):
#             if res[-1][1] >= intervals[i][0]:
#                 res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
#             else:
#                 if i == index:
#                     res.append(intervals[i])
#                 else:
#                     res.extend(intervals[i:])
#                     break
#         return res
#
#
# s = Solution()
# print(s.insert(intervals = [[0,5],[9,12]], newInterval = [7, 16]))

a = [3, 5]
print(a)
a[0], a[1] = a[1], a[0]
print(a)