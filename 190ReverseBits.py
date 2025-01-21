from re import split


class Solution:
    def reverseBits(self, n: int) -> int:
        if not n:
            return 0
        n = abs(n)
        n = bin(n)
        n = n[2:]
        if (l:=len(n))<32:
            n = ("0" * (32-l)) + n
        n = n[::-1]
        while n[0] == '0':
            n = n[1:]
        n = "0b" + n

        return int(n,2) #todo: optimize


x = Solution().reverseBits(43261596)