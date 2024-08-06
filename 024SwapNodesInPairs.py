from typing import Optional
from DataStructures.ListNode import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swapPairsHelper(head, 0)

    def swapPairsHelper(self, head, i: int):
        if head is None:
            return None

        if head.next is None:
            return head

        h = ListNode(head.val, head.next)
        n = ListNode(head.next.val, head.next.next)
        x = ListNode(head.next.next.val, head.next.next.next) if (n.next is not None) else None

        print([str(z) for z in [h, n, x]])

        if i % 2:

            h.next = self.swapPairsHelper(n, i + 1)
            return h
        else:
            n.next = h
            h.next = self.swapPairsHelper(h, i + 1)
            return n


nodes2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# nodes = []
# nodes2 = [0]
# todo

u = ListNode().getRootFromArray(nodes2)

r = Solution().swapPairs(u)
while r:
    print(r)
    r = r.next

# https://leetcode.com/problems/swap-nodes-in-pairs
