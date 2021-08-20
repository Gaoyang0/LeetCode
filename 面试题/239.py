from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # # 单调栈
        # '''
        # 窗口在滑动的时候会删除一个数，加入一个数
        # 这个过程有个非常影藏且有用的规则：后加入窗口的数，会在是此刻窗口中最后一个被删除的数，
        # 因此，窗口中比加入的数小的数就没有用了（也就是不会成为后续窗口中的最大值）
        # '''
        # from collections import deque
        #
        # if len(nums) <= 1 or k <= 1:
        #     return nums
        #
        # # 双端递减队列
        # diminishing_queue = deque()
        # diminishing_queue.append(nums[0])
        # res = []
        # for i in range(1, len(nums)):
        #     # nums[i]是要加入的， nums[i-k]是要删除的
        #     while len(diminishing_queue) > 0 and diminishing_queue[-1] < nums[i]:
        #         diminishing_queue.pop()
        #     diminishing_queue.append(nums[i])
        #
        #     if i >= k:
        #         if nums[i - k] == diminishing_queue[0]:
        #             # 队列从前往后既是升序，也是按照nums顺序，如果队列头部刚好是此次滑动要删除的，
        #             # 那么除队后面的肯定是在窗口内的，不需要考虑删除
        #             diminishing_queue.popleft()
        #     if i >= k-1:
        #         res.append(diminishing_queue[0])
        # return res

        # 大根堆
        # 存下标, 可使用比较下标大小的方式来判断是否在窗口内
        class MaxRootHeap:
            def __init__(self):
                pass

            # 向下调整
            # 调整列表中的元素并保证以root为根的堆是一个大根堆
            def shift_down(self, heap, heapSize, root):
                # 递归实现
                # 传入heapSize的原因是：堆排序需要原地指定堆的大小
                '''
                给定某个节点的下标root，这个节点的父节点、左子节点、右子节点的下标都可以被计算出来。
                父节点：(root-1)//2
                左子节点：2*root + 1
                右子节点：2*root + 2  即：左子节点 + 1
                '''
                left = 2 * root + 1
                right = left + 1

                # 得到max(root, left, right)
                larger = root
                if left < heapSize and heap[larger] < heap[left]:
                    larger = left
                if right < heapSize and heap[larger] < heap[right]:
                    larger = right

                # 如果做了堆调整则larger的值等于左节点或者右节点的值，这个时候做堆调整操作
                if larger != root:
                    # 交换
                    heap[larger], heap[root] = heap[root], heap[larger]
                    # 递归的对子树做调整, 交换后可能影响子树的堆结构，需要递归
                    self.shift_down(heap, heapSize, larger)

            def shift_up(self, heap, root):
                # 非递归实现
                # 对于某个结点i，将其与父节点：(root-1)//2，如果i的值大于父节点的值，则交换两个结点的位置，
                # 重复上述步骤，直到新结点的值不再大于父节点的值或者新结点成为根节点为止。
                p = root
                parent = lambda x: (x - 1) // 2 if x - 1 >= 0 else 0
                tmp = heap[p]
                # p为非根节点且父节点比插入的值小
                while p > 0 and heap[parent(p)] < tmp:
                    heap[p] = heap[parent(p)]
                    p = parent(p)
                heap[p] = tmp

            def build_heap(self, heap):
                heapSize = len(heap)
                # 自底向上建堆，从最后一个非叶子结点开始：(heapSize - 2) // 2
                for i in range((heapSize - 2) // 2, -1, -1):
                    self.shift_down(heap, heapSize, i)

            def insert(self, heap, node):
                heap.append(node)
                self.shift_up(heap, len(heap) - 1)

            # 删除堆顶
            def remove_max(self, heap):
                if (len(heap) == 0):
                    return None
                else:
                    tmp = heap[0]
                    # 把最后位置的元素放在堆顶，然后向下调整
                    heap[0] = heap[-1]
                    heap.pop()
                    if (len(heap) > 1):
                        self.shift_down(heap, len(heap), 0)
                    return tmp

            # 删除任意节点
            # 将完全二叉树最末尾结点m和待删除结点p交换位置，删除结点p，先用结点m与其父节点进行比较
            # 如果该结点的值大于父节点的值，则采用向上调整法；
            # 否则，用结点m与其左右子结点中值较大的一个进行比较，如果该结点的值小于该子节点的值，则采用向下调整法。
            def delete(self, heap, position):
                parent = lambda x: (x - 1) // 2 if x - 1 >= 0 else 0
                if position < 0 or position >= len(heap):
                    return False
                heap[position] = heap[-1]
                heap.pop()
                if position > 0 and heap[position] > heap[parent(position)]:
                    self.shift_up(heap, position)
                else:
                    self.shift_down(heap, len(heap), position)
                return True

        max_root_heap = MaxRootHeap()
        if len(nums) <= 1 or k <= 1:
            return nums

        heap_array = nums[:k]
        max_root_heap.build_heap(heap_array)
        res = [heap_array[0]]

        for i in range(k, len(nums)):
            max_root_heap.insert(heap_array, nums[i])
            # 这里如果存的是下标，可使用比较下标大小的方式来判断是否在窗口内，就不会超时
            while heap_array[0] not in  set(nums[i-k+1:i+1]):
                max_root_heap.remove_max(heap_array)
            res.append(heap_array[0])
        return res




s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
# print(s.maxSlidingWindow([1], 1))
# print(s.maxSlidingWindow([9, 11], 2))
# print(s.maxSlidingWindow([7,2,4], 2))
# print(s.maxSlidingWindow([8,7,9,2,4], 2))