def insert_sort(myList):
    # 获取列表长度
    length = len(myList)

    for i in range(1, length):
        temp = myList[i]
        # 继续往前寻找,如果有比临时变量大的数字,则后移一位,直到找到比临时变量小的元素或者达到列表第一个元素
        j = i - 1
        while j >= 0 and myList[j] > temp:
            myList[j + 1] = myList[j]
            j = j - 1
        # 将临时变量赋值给本次最合适的位置
        myList[j + 1] = temp


myList = [49, 38, 65, 97, 76, 13, 27, 49]

insert_sort(myList)
print(myList)