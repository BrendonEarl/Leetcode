from DataStructures.ListNode import ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sol = Solution()

        firstVal, firstCarryDigit = sol.addNodes(l1.val, l2.val)
        firstNode = ListNode(firstVal)

        test = sol.addTwoNumbersHelper(l1.next, l2.next, ListNode(None, None), firstCarryDigit)

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
        return [smallDigit := sum % 10, int((sum - smallDigit) / 10)]

    def printNode(self, firstNode):
        t = firstNode
        while True:
            if t:
                print(t.val)
                t = t.next
            else:
                break

# https://leetcode.com/problems/add-two-numbers
