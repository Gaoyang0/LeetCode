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


# 好记版
def q_s(arr):
    if len(arr) <= 1:
        return arr

    mid = arr[len(arr) // 2]
    l = [i for i in arr if i < mid]
    m = [i for i in arr if i == mid]
    r = [i for i in arr if i > mid]

    return q_s(l) + m + q_s(r)


# arr = [10, 7, 8, 9, 1, 5]
arr = [10, 7, 8, 9, 1, 1]
# n = len(arr)
# quick_sort(arr, 0, n - 1)
# print(arr)

print(q_s(arr))