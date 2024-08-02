from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val} {self.next.val if self.next else self.next}'


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while None in lists:
            lists.remove(None)
        if not lists:
            return None

        minIndex, minVal = 0, None
        for i,l in enumerate(lists):
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
nodes3 = [-1,60,61,62]
# nodes = []
# nodes2 = [0]
# todo more efficient

def xyzHelper(nodeList, index):
    if index >= len(nodeList):
        return None
    return ListNode(nodeList[index], xyzHelper(nodeList, index + 1))

def xyz(arr):
    return xyzHelper(arr, 0)

t = xyz(nodes)
u = xyz(nodes2)
v = xyz(nodes3)

r = Solution().mergeKLists([t, u, v, None])
while r:
    print(r)
    r = r.next

# https://leetcode.com/problems/merge-k-sorted-lists
