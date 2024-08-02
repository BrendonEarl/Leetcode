from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val} {self.next.val if self.next else self.next}'


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass

#todo

# https://leetcode.com/problems/reverse-nodes-in-k-group
