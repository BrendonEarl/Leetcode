from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        pass
    # todo: do


troot = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

