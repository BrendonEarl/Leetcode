# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from DataStructures.ListNode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        return self.reverseListHelper(head)


    def reverseListHelper(self, head: Optional[ListNode]):
        if head is None:
            return None
        if head.next is None:
            head
        n = head.next
        z = self.reverseListHelper(head.next)
        #todo: reverse linkedlist without putting vals into an array

        return head



s = ListNode().getRootFromArray([1,2,3,4,5])
x = Solution().reverseList(s)