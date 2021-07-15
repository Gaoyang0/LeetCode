def bubble_sort(arr):
    while True:
        i = 0
        flag = False
        while i < len(arr)-1:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True
            i += 1
        if not flag:
            break


if __name__ == "__main__":
    arr = [49, 38, 65, 97, 76, 13, 27, 49]
    bubble_sort(arr)
    print(arr)
