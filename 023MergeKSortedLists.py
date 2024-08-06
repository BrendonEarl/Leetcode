from typing import Optional, List
from DataStructures.ListNode import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while None in lists:
            lists.remove(None)
        if not lists:
            return None

        minIndex, minVal = 0, None
        for i, l in enumerate(lists):
            if (minVal is None) or l.val < minVal:
                minIndex = i
                minVal = l.val

        list0 = lists[minIndex]
        lists[minIndex] = lists[minIndex].next

        list0.next = self.mergeKListsHelper(lists, list0)
        return list0

    def mergeKListsHelper(self, lists: List[Optional[ListNode]], list0: Optional[ListNode]):
        while None in lists:
            lists.remove(None)

        if not lists:
            return None

        minIndex, minVal = 0, None
        for i, l in enumerate(lists):
            if (minVal is None) or l.val < minVal:
                minIndex = i
                minVal = l.val

        list0 = lists[minIndex]
        lists[minIndex] = lists[minIndex].next

        list0.next = self.mergeKListsHelper(lists, list0)
        return list0


nodes = [1, 2, 5, 9, 13, 15, 100]
nodes2 = [0, 3, 5, 8, 13, 13, 14]
nodes3 = [-1, 60, 61, 62]


# nodes = []
# nodes2 = [0]
# todo more efficient

ln = ListNode()
t = ln.getRootFromArray(nodes)
u = ln.getRootFromArray(nodes2)
v = ln.getRootFromArray(nodes3)

r = Solution().mergeKLists([t, u, v, None])
while r:
    print(r)
    r = r.next

# https://leetcode.com/problems/merge-k-sorted-lists
