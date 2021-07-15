# 148

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 解法一，模仿插入排序
        # if not head:
        #     return head
        #
        # p = head.next
        # head.next = None
        # h = ListNode(0, head)
        # while p:
        #     # 找到对应位置插入
        #     temp = p.next
        #     pre = h
        #     q = pre.next
        #     while q and q.val < p.val:
        #         pre = pre.next
        #         q = q.next
        #     p.next = pre.next
        #     pre.next = p
        #     p = temp
        # return h.next

        # 归并排序递归
        # 递归结束条件
        if not head or not head.next:
            return head

        # 快慢指针找到中点(原理是fast的速度是slow的两倍)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow即为中点
        mid = slow.next
        # 将前半部分链表截断
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        # 合并
        h = p = ListNode(0, None)
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left if left else right
        return h.next


def stringToListNode(numbers):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    numbers = [1, 3, -3, 7, 2]
    head = stringToListNode(numbers)
    ret = Solution().sortList(head)
    out = listNodeToString(ret)
    print(out)


if __name__ == '__main__':
    main()
