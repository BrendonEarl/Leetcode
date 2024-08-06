from typing import Optional
from DataStructures.ListNode import ListNode


class Solution:
    counter = 0

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.removeNthHelper(head, n)

    def removeNthHelper(self, node: Optional[ListNode], n) -> Optional[ListNode]:
        if node is None:
            self.counter += 1
            return None

        else:
            node.next = self.removeNthHelper(node.next, n)

            if self.counter > 0:
                if n == self.counter:
                    self.counter += 1
                    return node.next
                else:
                    self.counter += 1
                    return node


nodes = [1, 2]

ln = ListNode()
t = ln.getRootFromArray(nodes)

r = Solution().removeNthFromEnd(t, 1)
print(r)

# https://leetcode.com/problems/remove-nth-node-from-end-of-list
