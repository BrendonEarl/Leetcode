"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros."""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sol = Solution()

        firstVal, firstCarryDigit = sol.addNodes(l1.val, l2.val)
        firstNode = ListNode(firstVal)

        test = sol.addTwoNumbersHelper(
            l1.next, l2.next, ListNode(None, None), firstCarryDigit)
        if test.val is not None:
            firstNode.next = test

        return firstNode

    def addTwoNumbersHelper(self, l1, l2, node, carry_digit):

        if not l1 and not l2:
            node.val = carry_digit if carry_digit else None
            return node

        else:
            node.val, carry = self.addNodes(
                l1.val if l1 else 0, l2.val if l2 else 0, carry_digit)

        test = self.addTwoNumbersHelper(
            l1.next if l1 else None, l2.next if l2 else None, ListNode(), carry)

        if test.val is not None:
            node.next = test
        return node

    def addNodes(self, oneVal, twoVal, threeval=0):
        sum = oneVal+twoVal+threeval
        return [smallDigit := sum % 10, (int)((sum-smallDigit)/10)]

    def printNode(self, firstNode):
        t = firstNode
        while True:
            if t:
                print(t.val)
                t = t.next
            else:
                break
# one = [0]
# two = [0]
# primaryNodes = []

# for list in one, two:
#     first = True
#     nNode = None
#     for index in range(len(list)):
#         if (not nNode):
#             if (index+1 >= len(list)):
#                 newNode = ListNode(list[index], None)
#             else:
#                 newNode = ListNode(list[index], nNode := ListNode(list[index+1]))

#             if first:
#                 primaryNodes.append(newNode)
#                 first = False
#         else:
#             tNode = nNode
#             if (index+1 >= len(list)):
#                 tNode.val,tNode.next = list[index], None
#             else:
#                 tNode.val,tNode.next = list[index], (nNode := ListNode(list[index+1]))

# print(Solution.addTwoNumbers(Solution, primaryNodes[0], primaryNodes[1]))


link = 'https://leetcode.com/problems/add-two-numbers'