# Definition for singly-linked list.
import json
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def reverse(hair, k):
            cnt = 0
            h = ListNode()
            p = hair
            while p and cnt < k:
                temp = p.next
                p.next = h.next
                h.next = p
                p = temp
                cnt += 1
            return h.next, p

        h = ListNode()
        p = head
        ha, tail = reverse(p, k)
        h.next = ha
        p = tail
        while p:
            ha, tail = reverse(p, k)

            print(listNodeToString(ha))
            h = ""
            break
        # return reverse(head, k)




def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

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
    line = "[1,2,3,4,5]"
    head = stringToListNode(line)
    k = 2

    ret = Solution().reverseKGroup(head, k)

    out = listNodeToString(ret)
    print(out)



if __name__ == '__main__':
    main()