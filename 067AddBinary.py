
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        one,two = a[::-1],b[::-1]
        r = 0
        i = 0
        x = ''
        while i < len(one) or i < len(two):
            if i < len(one) and i < len(two):
                if one[i] and two[i]:
                    pass

# todo complete
Solution().addBinary(a = "1010", b = "1011")