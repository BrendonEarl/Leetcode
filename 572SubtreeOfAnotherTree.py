from typing import Optional
from DataStructures.TreeNode import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSubtreeHelper(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot) if root.left else False
        right = self.isSubtree(root.right, subRoot) if root.right else False

        return left or right

    def isSubtreeHelper(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if root is None and subRoot is None:
            return True
        if root is None:
            return False
        if subRoot is None:
            return False
        return root.val == subRoot.val and self.isSubtreeHelper(root.left, subRoot.left) and self.isSubtreeHelper(root.right, subRoot.right)

# https://leetcode.com/problems/subtree-of-another-tree
