from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val} {self.next.val if self.next else self.next}'


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swapPairsHelper(head, 0)

    def swapPairsHelper(self, head, i: int):
        if head is None:
            return None

        if head.next is None:
            return head

        h = ListNode(head.val,head.next)
        n = ListNode(head.next.val, head.next.next)
        x = ListNode(head.next.next.val, head.next.next.next) if (n.next is not None) else None

        print([str(z) for z in [h, n, x]])

        if i % 2:

            h.next = self.swapPairsHelper(n, i+1)
            return h
        else:
            n.next = h
            h.next = self.swapPairsHelper(h, i+1)
            return n




nodes2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# nodes = []
# nodes2 = [0]
#todo


def xyzHelper(nodeList, index):
    if index >= len(nodeList):
        return None
    return ListNode(nodeList[index], xyzHelper(nodeList, index + 1))


def xyz(arr):
    return xyzHelper(arr, 0)


# t = xyz(nodes)
u = xyz(nodes2)

# print(f'{t} {u}')
r = Solution().swapPairs(u)
while r:
    print(r)
    r = r.next
