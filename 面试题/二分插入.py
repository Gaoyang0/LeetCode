def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low


a = [1, 3, 7, 9, 14, 20, 24]
print(binary_search(a, 0))  # 0
print(binary_search(a, 1))  # 0
print(binary_search(a, 2))  # 1
print(binary_search(a, 4))  # 2
print(binary_search(a, 8))  # 3

print(binary_search(a, 11))  # 4
print(binary_search(a, 16))  # 5
print(binary_search(a, 24))  # 6
print(binary_search(a, 29))  # 7

# a = [1, 3, 6, 8, 12]
# print(binary_search(a, 4))  # 0
# # print(binary_search(a, 9))  # 3
# # print(binary_search(a, 24))  # 6
# # print(binary_search(a, 11))  # 4