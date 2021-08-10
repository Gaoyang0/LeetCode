from typing import List


class MaxHeap:
    # 大根堆
    def adjust_max_heap(self, heap, heapSize, root):
        '''
        root左儿子节点位置root*2 + 1
        root右儿子节点位置root*2 + 2
        root父亲节点位置(root-1) // 2
        '''
        left = root * 2 + 1
        right = root * 2 + 2
        larger = root
        if left < heapSize and heap[larger] < heap[left]:
            larger = left
        if right < heapSize and heap[larger] < heap[right]:
            larger = right
        if larger != root:
            heap[larger], heap[root] = heap[root], heap[larger]
            self.adjust_max_heap(heap, heapSize, larger)

    # 建堆
    def build_max_heap(self, heap):
        # 从最后一个非叶子结点开始调整
        # 最后一个非叶子结点的位置 (len(heap) - 2) // 2
        for i in range((len(heap) - 2) // 2, -1, -1):
            self.adjust_max_heap(heap, len(heap), i)

    def get_max_k(self, nums, k):
        self.build_max_heap(nums)
        for i in range(len(nums) - 1, (len(nums) - k) - 1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.adjust_max_heap(nums, i, 0)

        return nums[-k:]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = MaxHeap()
        return max_heap.get_max_k(nums, k)[0]











s = Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
# print(s.findKthLargest([2,1], 1))
# print(s.findKthLargest([2,1], 2))
