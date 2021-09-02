# -*- coding:utf-8 -*-
# Author:DaoYang


def quick_sort(arr, start, end):
    """快速排序"""
    # 递归的退出条件
    if start >= end:
        return

    mid = arr[start]
    low = start
    high = end

    while low < high:
        while low < high and arr[high] >= mid:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] < mid:
            low += 1
        arr[high] = arr[low]
    arr[low] = mid

    quick_sort(arr, start, low - 1)
    quick_sort(arr, low + 1, end)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n - 1)
print(arr)