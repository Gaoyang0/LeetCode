

# def my_sort(arr):
#     for i in range(1, len(arr)):
#         temp = arr[i]
#         j = i-1
#         while j >= 0 and arr[j] > temp:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = temp
#
#
# a = [2,1,4,1,7]
#
# print(a)
# my_sort(a)
# print(a)

# 快速排序

def quick_sort(arr, start, end):
    if start >= end:
        return

    mid = arr[start]
    low, high = start, end

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

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)


