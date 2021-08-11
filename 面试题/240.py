from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        首先，我们初始化一个指向矩阵左下(右上也可以)角的 (row，col)(row，col) 指针。
        然后，直到找到目标并返回 true（或者指针指向矩阵维度之外的 (row，col)(row，col) 为止，
        我们执行以下操作：如果当前指向的值大于目标值，则可以 “向上” 移动一行。
        否则，如果当前指向的值小于目标值，则可以移动一列。不难理解为什么这样做永远不会删减正确的答案；
        因为行是从左到右排序的，所以我们知道当前值右侧的每个值都较大。
        因此，如果当前值已经大于目标值，我们知道它右边的每个值会比较大。
        也可以对列进行非常类似的论证，因此这种搜索方式将始终在矩阵中找到目标（如果存在）。
        '''
        # 初始化为左下角
        # row, col = (len(matrix)-1, 0)
        # while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        #     if matrix[row][col] == target:
        #         return True
        #     elif matrix[row][col] > target:
        #         # 因为每行是升序，所以排除比row大的行
        #         row -= 1
        #     else:
        #         # 因为每列是升序，所以排除比col小的列
        #         col += 1
        # return False

        # 逐行二分查找
        def binary_search(nums, target):
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    return True
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False
        for row in matrix:
            if row[0] <= target <= row[-1]:
                if binary_search(row, target):
                    return True
        return False





s = Solution()
print(s.searchMatrix( [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 4))