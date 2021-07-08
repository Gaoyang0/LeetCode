from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        p_last = m+n-1
        while p1>=0 and p2>=0 and p_last >= m:
            if nums1[p1] <= nums2[p2]:
                nums1[p_last] = nums2[p2]
                p2 -= 1
            else:
                nums1[p_last] = nums1[p1]
                nums1[p1] = nums2[p2]
            p_last -= 1

        # if p1>0
        return nums1


s = Solution()
print(s.merge([7,9,0,0,0],2, [2,5,6],  3))
# print(s.merge([1,2,3,0,0,0],3, [2,5,6],  3))