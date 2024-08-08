from typing import Optional, List

from DataStructures.TreeNode import TreeNode


class Solution:

    def __init__(self):
        self.vals = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        self.rightSideViewHelper(root, 0)
        return self.vals

    def rightSideViewHelper(self, node, height):
        if node is None:
            return

        if height >= len(self.vals):
            self.vals.append(node.val)

        self.rightSideViewHelper(node.right, height+1)
        self.rightSideViewHelper(node.left, height+1)


froot = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))

a = Solution().rightSideView(froot)
print(a)

# https://leetcode.com/problems/binary-tree-right-side-view