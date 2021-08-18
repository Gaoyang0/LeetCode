# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        def merge(l1, l2):
            h = ListNode(-1)
            p = h
            p1, p2 = l1, l2
            while p1 and p2:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next

            p.next = p1 if p1 else p2
            return h.next

        p = lists[0]
        for l in lists[1:]:
            if l:
                p = merge(p, l)
        return p






# [[1,4,5],[1,3,4],[2,6]]
