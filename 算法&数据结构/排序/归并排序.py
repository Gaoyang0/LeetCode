# -*- coding:utf-8 -*-
# Author:DaoYang


def merge_sort(list):
    # 不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
    if len(list) == 1:
        return list
    # // =（向下取整）
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    # 对拆分过后的左右再拆分 一直到只有一个元素为止
    left_list = merge_sort(left)
    right_list = merge_sort(right)
    # l,r有序,将l,r进行合并
    return merge(left_list, right_list)


# 合并两个有序的列表
def merge(left_list, right_list):
    # 从两个有顺序的列表里边依次取数据比较后放入result
    # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
    result = []
    while len(left_list) > 0 and len(right_list) > 0:
        # 为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
        if left_list[0] <= right_list[0]:
            result.append(left_list.pop(0))
        else:
            result.append(right_list.pop(0))
    # while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    result += left_list
    result += right_list
    return result


if __name__ == '__main__':
    list = [4, 1, 5, 3, 2]
    print(merge_sort(list))
# [4, 1, 5, 3, 2]=>[4, 1] [5, 3, 2]
# [4, 1]=>[4] [1]=>[1, 4]
# [5, 3, 2]=>[5] [3, 2]
# [5]=>[5] [3, 2]=>[3] [2]=> [2, 3]
# [5] [2, 3]=>[2, 3, 5]
# [1, 4] [2, 3, 5]=>[1, 2, 3, 4, 5]