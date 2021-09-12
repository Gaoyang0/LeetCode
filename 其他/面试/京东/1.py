n = int(input().strip())
nums = list(map(int, input().strip().split(" ")))

def max_diff(n, arr):
    arr.sort()
    h, t, flag, res = 0, n-1, 0, 0
    temp = []
    while h<=t:
        if flag == 0:
            if len(temp) > 0 and temp[-1] == arr[h]:
                temp.insert(0, arr[h])
            else:
                temp.append(arr[h])
            flag = 1
            h += 1
        else:
            if len(temp) > 0 and temp[-1] == arr[t]:
                temp.insert(0, arr[t])
            else:
                temp.append(arr[t])
            flag = 0
            t -= 1


    h, t, flag, res2 = 0, n - 1, 0, 0

    temp2 = []
    while h<=t:
        if flag == 0:
            if len(temp2) > 0 and temp2[-1] == arr[t]:
                temp2.insert(0, arr[t])
            else:
                temp2.append(arr[t])
            flag = 1
            t -= 1
        else:
            if len(temp2) > 0 and temp2[-1] == arr[h]:
                temp2.insert(0, arr[h])
            else:
                temp2.append(arr[h])
            flag = 0
            h += 1
    for i in range(n-1):
        res += abs(temp[i]- temp[i+1])

    for i in range(n - 1):
        res2 += abs(temp2[i] - temp2[i + 1])
    return max(res, res2)

print(max_diff(n, nums))


