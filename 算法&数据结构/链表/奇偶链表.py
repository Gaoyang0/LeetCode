class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 头插法，偶数跳过
        p = head
        pre = head

        index = 0
        while p:
            s = listNodeToString(head)
            index += 1
            if index == 2 or index == 1:
                p = p.next
                continue
            if index % 2 != 0:

                temp = p.next
                p.next = pre.next
                pre.next.next = temp
                pre.next = p
                pre = p
                p = temp
            else:
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
    line = [1, 2, 3, 4, 5]
    head = stringToListNode(line)
    ret = Solution().oddEvenList(head)
    out = listNodeToString(ret)
    print(out)


if __name__ == '__main__':
    main()
