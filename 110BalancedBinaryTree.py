from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return bool(self.isBalancedHelper(root))

    def isBalancedHelper(self, node):
        if node is None:
            return 1

        l = self.isBalancedHelper(node.left)
        r = self.isBalancedHelper(node.right)

        if (l and r) and (abs(l - r) <= 1):
            return 1 + max(l, r)
        else:
            return False


troot = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
froot = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))

print(Solution.isBalanced(Solution(),froot))
