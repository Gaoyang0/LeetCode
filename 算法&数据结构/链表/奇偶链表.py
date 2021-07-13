# 328
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        p = head
        tail = head
        pre = head
        index = 0
        while p:
            index += 1
            if index % 2 != 0 and index > 2:
                temp = p.next
                pre.next = p.next
                p.next = tail.next
                tail.next = p
                tail = p
                p = temp
            else:
                pre = p
                p = p.next
        return head


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
    line = [1, 2, 3, 4, 5, 6, 7]
    head = stringToListNode(line)
    ret = Solution().oddEvenList(head)
    out = listNodeToString(ret)
    print(out)


if __name__ == '__main__':
    main()
