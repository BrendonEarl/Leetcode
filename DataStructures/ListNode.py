class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val} {self.next.val if self.next else self.next}'

    def __getRootFromArray(self, nodeList, index):
        if index >= len(nodeList):
            return None
        return ListNode(nodeList[index], self.__getRootFromArray(nodeList, index + 1))

    def getRootFromArray(self, arr):
        return self.__getRootFromArray(arr, 0)
