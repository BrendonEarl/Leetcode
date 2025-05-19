
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        long, short =  (b[::-1], a[::-1]) if len(b) > len(a) else (a[::-1] , b[::-1])

        remainder = 0
        index = 0
        backwards = ''

        while index < len(long):
            
            digit1 = long[index]
            digit2 = short[index] if index < len(short) else '0'
            add = 0
            if digit1 == '1':
                add += 1
            if digit2 == '1':
                add += 1
            if remainder > 0:
                add += 1
                remainder -= 1
            if add > 1:
                remainder += 1

            if add % 2:
                backwards += '1'
            else:
                backwards += '0'


            index+=1
        if remainder > 0:
            backwards += '1'

        return backwards[::-1]


Solution().addBinary(a = "1010", b = "1011")