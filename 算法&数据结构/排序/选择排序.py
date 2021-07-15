def select_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


if __name__ == "__main__":
    arr = [-3, 38, 65, 97, 76, 13, 27, -1]
    select_sort(arr)
    print(arr)