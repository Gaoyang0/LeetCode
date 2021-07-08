# leetcode 142


# 快指针的路程f, 慢指针的路程s, 环状的长度L, 环状以外的长度为a, 则有f-s = n*L
# 速度是两倍的关系, 则有f = 2 * s
# 所以s = n*L
# 又因为s = a + (n-1)*L + b = n * L
# 所以a + b = L
# 有因为b + c = L
# 所以a = c


class ListNode():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return None
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
b = ListNode(2, ListNode(0, ListNode(-4, )))
head = ListNode(3, b)

p = head
while p:
    if p.next is None:
        p.next = b
        break
    p = p.next
# p = head
# while p:
#     print(p.data)
#     p = p.next
s = Solution()
print(s.detectCycle(head).data)