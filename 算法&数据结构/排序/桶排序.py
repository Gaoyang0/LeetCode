from typing import List

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
    return myList


def bucket_sort(arr:List[int]):
    """桶排序"""
    min_num = min(arr)
    max_num = max(arr)
    # 桶的大小
    bucket_range = (max_num-min_num) / len(arr)
    # 桶数组
    count_list = [[] for i in range(len(arr) + 1)]
    # 向桶数组填数
    for i in arr:
        count_list[int((i-min_num)//bucket_range)].append(i)
    arr.clear()
    # 回填，这里桶内部排序直接调用了sorted
    for i in count_list:
        for j in insert_sort(i):
            arr.append(j)


if __name__ == '__main__':
    import random
    random.seed(54)
    arr = [random.randint(0,100) for _ in range(10)]
    print("原始数据：", arr)
    bucket_sort(arr)
    print("桶排序结果：", arr)
