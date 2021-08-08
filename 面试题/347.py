from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # import heapq
        # d = dict()
        # for i in nums:
        #     if i not in d:
        #         d[i] = 0
        #     d[i] += 1
        #
        # temp = heapq.nlargest(k, d.items(), key=lambda x:x[1])
        # return [i[0] for i in temp]

        # 自己建堆
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1

        # 向下调整
        def max_heapify(heap, heapSize, root):  # 调整列表中的元素并保证以root为根的堆是一个大根堆
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
            if left < heapSize and heap[larger][1] < heap[left][1]:
                larger = left
            if right < heapSize and heap[larger][1] < heap[right][1]:
                larger = right

            # 如果做了堆调整则larger的值等于左节点或者右节点的值，这个时候做堆调整操作
            if larger != root:
                # 交换
                heap[larger], heap[root] = heap[root], heap[larger]
                # 递归的对子树做调整, 交换后可能影响子树的堆结构，需要递归
                max_heapify(heap, heapSize, larger)

        def build_max_heap(heap):
            heapSize = len(heap)
            # 自底向上建堆，从最后一个非叶子结点开始：(heapSize - 2) // 2
            for i in range((heapSize - 2) // 2, -1, -1):
                max_heapify(heap, heapSize, i)

        res = []
        heap = [(k, v) for k, v in d.items()]
        build_max_heap(heap)
        # 调整后列表的第一个元素就是这个列表中最大的元素，将其与最后一个元素交换，然后将剩余的列表再递归的调整为最大堆
        for i in range(len(heap) - 1, len(heap) - 1 - k, -1):
            heap[0], heap[i] = heap[i], heap[0]
            res.append(heap[i][0])
            # 修改堆大小继续调整，得到最大值
            max_heapify(heap, i, 0)
        return res




s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))