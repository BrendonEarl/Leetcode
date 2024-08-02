from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val} {self.next.val if self.next else self.next}'


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

def xyzHelper(nodeList, index):
    if index >= len(nodeList):
        return None
    return ListNode(nodeList[index], xyzHelper(nodeList, index + 1))


def xyz(arr):
    return xyzHelper(arr, 0)


t = xyz(nodes)

r = Solution().removeNthFromEnd(t, 1)
print(r)

# https://leetcode.com/problems/remove-nth-node-from-end-of-list
