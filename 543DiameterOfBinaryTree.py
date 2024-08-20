from typing import Optional
from DataStructures.TreeNode import TreeNode


class Solution:
    longest = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameterHelper(root)
        return self.longest
    def diameterHelper(self, node):
        if node is None:
            return 0

        l = 1 + self.diameterHelper(node.left)
        r = 1 + self.diameterHelper(node.right)
        if (x:=(l+r-2)) > self.longest:
            self.longest = x

        return max(l,r)



troot = TreeNode().getRootFromArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,None,None,5,None,None,None,None,None,9])
s = Solution().diameterOfBinaryTree(troot)
print(s)

# https://leetcode.com/problems/diameter-of-binary-tree
