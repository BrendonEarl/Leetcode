from typing import Optional
from DataStructures.ListNode import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (not list2):
            return list1 if list1 else list2

        if list1.val <= list2.val:
            list0 = list1
            list1 = list1.next
        else:
            list0 = list2
            list2 = list2.next

        list0.next = self.mergeTwoListsHelper(list1, list2, list0)
        return list0

    def mergeTwoListsHelper(self, list1: Optional[ListNode], list2: Optional[ListNode], list0: Optional[ListNode]):
        if (list1 is None) or (list2 is None):
            if (list1 is None) and (list2 is None):
                return None
            if list1:
                list0 = list1
                list1 = list1.next
            else:
                list0 = list2
                list2 = list2.next
        else:
            if list1.val <= list2.val:
                list0 = list1
                list1 = list1.next
            else:
                list0 = list2
                list2 = list2.next

        list0.next = self.mergeTwoListsHelper(list1, list2, list0)
        return list0


nodes = [1, 2, 5, 9, 13, 15]
nodes2 = [0, 3, 5, 8, 13, 13, 14]

ln = ListNode()
t = ln.getRootFromArray(nodes)
u = ln.getRootFromArray(nodes2)

r = Solution().mergeTwoLists(t, u)
while r:
    print(r)
    r = r.next

# https://leetcode.com/problems/merge-two-sorted-lists
