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
        parent = lambda x : (x-1) // 2 if x - 1 >= 0 else 0
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


heap_array = [47, 50, 57, 77, 77, 78, 94, 80, 45]
max_root_heap = MaxRootHeap()
max_root_heap.build_heap(heap_array)

# '''堆排序测试'''
# # 调整后列表的第一个元素就是这个列表中最大的元素，将其与最后一个元素交换，然后将剩余的列表再递归的调整为最大堆
# for i in range(len(heap_array) - 1, -1, -1):
#     heap_array[0], heap_array[i] = heap_array[i], heap_array[0]
#     # 修改堆大小继续调整，得到最大值
#     max_root_heap.shift_down(heap_array, i, 0)
# print(heap_array)

# '''插入测试'''
# print("建堆结果：", heap_array)
# max_root_heap.insert(heap_array, 100)
# print(heap_array)
# max_root_heap.insert(heap_array, 88)
# print(heap_array)
# max_root_heap.insert(heap_array, 10)
# print(heap_array)

# '''删除测试最大值'''
# print("建堆结果：", heap_array)
# max_root_heap.remove_max(heap_array)
# print(heap_array)
# max_root_heap.remove_max(heap_array)
# print(heap_array)

'''删除测试任意值'''
heap_array = [90,60,30,40,50,20,15,35]
max_root_heap = MaxRootHeap()
max_root_heap.build_heap(heap_array)
print("建堆结果：", heap_array)
# 向上调整
max_root_heap.delete(heap_array, 5)
print(heap_array)
# 向下调整
max_root_heap.delete(heap_array, 1)
print(heap_array)


