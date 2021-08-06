# -*- coding:utf-8 -*-
# Author:DaoYang

'''
大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]
小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]
一般升序采用大顶堆，降序采用小顶堆
'''

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
    if left < heapSize and heap[larger] < heap[left]:
        larger = left
    if right < heapSize and heap[larger] < heap[right]:
        larger = right

    # 如果做了堆调整则larger的值等于左节点或者右节点的值，这个时候做堆调整操作
    if larger != root:
        # 交换
        heap[larger], heap[root] = heap[root], heap[larger]
        # 递归的对子树做调整, 交换后可能影响子树的堆结构，需要递归
        max_heapify(heap, heapSize, larger)


# 构造一个堆，将堆中所有数据重新排序
def build_max_heap(heap):
    heapSize = len(heap)
    # 自底向上建堆，从最后一个非叶子结点开始：(heapSize - 2) // 2
    for i in range((heapSize - 2) // 2, -1, -1):
        max_heapify(heap, heapSize, i)


def heap_sort_ascend(heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行堆调整过程。
    build_max_heap(heap)
    # 调整后列表的第一个元素就是这个列表中最大的元素，将其与最后一个元素交换，然后将剩余的列表再递归的调整为最大堆
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        # 修改堆大小继续调整，得到最大值
        max_heapify(heap, i, 0)


# 向下调整
def min_heapify(heap, heapSize, root):
    # 调整列表中的元素并保证以root为根的堆是一个小根堆
    '''
    给定某个节点的下标root，这个节点的父节点、左子节点、右子节点的下标都可以被计算出来。
    父节点：(root-1)//2
    左子节点：2*root + 1
    右子节点：2*root + 2  即：左子节点 + 1
    '''
    left = 2 * root + 1
    right = left + 1

    # 得到min(root, left, right)
    smaller = root
    if left < heapSize and heap[smaller] > heap[left]:
        smaller = left
    if right < heapSize and heap[smaller] > heap[right]:
        smaller = right

    # 如果做了堆调整则smaller的值等于左节点或者右节点的值，这个时候做堆调整操作
    if smaller != root:
        # 交换
        heap[smaller], heap[root] = heap[root], heap[smaller]
        # 递归的对子树做调整, 交换后可能影响子树的堆结构，需要递归
        min_heapify(heap, heapSize, smaller)


def build_min_heap(heap):
    heapSize = len(heap)
    # 自底向上建堆，从最后一个非叶子结点开始：(heapSize - 2) // 2
    for i in range((heapSize - 2) // 2, -1, -1):
        min_heapify(heap, heapSize, i)


def heap_sort_descend(heap):
    build_min_heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        # 修改堆大小继续调整，得到最小值
        min_heapify(heap, i, 0)


if __name__ == '__main__':
    a = [47, 50, 57, 77, 77, 78, 94, 80, 45]
    print(a)
    heap_sort_ascend(a)
    print(a)
    heap_sort_descend(a)
    print(a)
