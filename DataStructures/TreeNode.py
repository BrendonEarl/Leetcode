class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val}'
        # return self.__str_help() #todo: print tree structure

    def getRootFromArray(self, arr):
        if not arr:
            return None
        return self.__getRootFromArray(0, arr)

    def __getRootFromArray(self, index, arr):
        if index >= len(arr) or (arr[index] is None):
            return None
        node = TreeNode(arr[index])
        node.left = self.__getRootFromArray((index * 2) + 1, arr)
        node.right = self.__getRootFromArray((index * 2) + 2, arr)

        return node

    def __str_help(self):
        mxdigits = self.__max_digits__()
        depth = self.__depth__()
        width = self.__width__()

        return str((mxdigits, depth, width))

    def __max_digits__(self):
        return self.__max_digits_help(self)

    def __max_digits_help(self, node):
        if node is None:
            return 0

        l = self.__max_digits_help(node.left)
        r = self.__max_digits_help(node.right)

        x = len(str(node.val))

        return max(l, r, x)

    def __width_help(self, node, pos, lr):
        if node is None:
            return lr

        lr = (min(pos, lr[0]), max(pos, lr[1]))
        l = self.__width_help(node.left, pos - 1, lr)
        r = self.__width_help(node.right, pos + 1, lr)

        return min(pos, l[0], r[0]), max(pos, l[1], r[1])

    def __width__(self):

        l, r = self.__width_help(self, 0, (0, 0))
        return (l, r)

    def __depth__(self):
        
        return self.__depth_help(self)

    def __depth_help(self, node):
        if node is None:
            return 0

        return 1 + max(self.__depth_help(node.left), self.__depth_help(node.right))

# tn = TreeNode()
# test = tn.getRootFromArray([3, 4, 5, 1, 2, None, None, None, None, 0])
# print(test)