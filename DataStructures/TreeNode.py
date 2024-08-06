class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def getRootFromArray(self, arr):
        if not arr:
            return None
        return self.__getRootFromArray(0, arr)

    def __getRootFromArray(self, index, arr):
        if index >= len(arr):
            return None
        node = TreeNode(arr[index])
        node.left = self.__getRootFromArray((index * 2) + 1, arr)
        node.right = self.__getRootFromArray((index * 2) + 2, arr)

        return node
