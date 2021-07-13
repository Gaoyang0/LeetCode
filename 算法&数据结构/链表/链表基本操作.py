# 61

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        l = 1
        p = head
        while p.next:
            p = p.next
            l += 1
        p.next = head

        pre = p
        p = head
        if k > l:
            k -= l * (k // l)
        for _ in range(l-k):
            pre = p
            p = p.next
        pre.next = None
        return p


def stringToListNode(numbers):
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
    numbers = [1, 2]
    k = 5

    head = stringToListNode(numbers)
    k = k

    ret = Solution().rotateRight(head, k)
    out = listNodeToString(ret)
    print(out)


if __name__ == '__main__':
    main()
