class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 解法一，模仿插入排序
        if not head:
            return head

        p = head.next
        head.next = None
        ph = ListNode(0, head)
        while p:
            s1 = listNodeToString(head)
            s2 = listNodeToString(p)
            # 找到对应位置插入
            q = p.next
            pre = ph
            if p.val < pre.next.val:
                p.next = head
                head = p

            while pre.next and pre.next.val < p.val:
                pre = pre.next
            p.next = pre.next
            pre.next = p
            p = q
        return head


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
    numbers = [-1, 5, -3, 4, 0]
    head = stringToListNode(numbers)
    ret = Solution().sortList(head)
    out = listNodeToString(ret)
    print(out)


if __name__ == '__main__':
    main()
