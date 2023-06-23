

class Solution:

    def reverse(self, x: int) -> int:
        li = (str)(x)
        if li[0] == (neg_sign := '-'):
            neg = True
            li = li[1:]
        else:
            neg = False

        point, reverse = 0, li[-1::-1]

        while reverse[point] == '0':
            point += 1
            if point == len(reverse):
                point -= 1
                break

        nl = neg_sign+(reverse[point:]) if neg else reverse[point:]

        return int(self.is_32bit_signed_integer(nl))

    def is_32bit_signed_integer(self, n: str):
        min_value = '-2147483648'
        max_value = '2147483647'
        compare_val = min_value if n[0] == '-' else max_value

        if (nlen := len(n)) < (clen := len(compare_val)):
            return n
        elif nlen > clen:
            return '0'
        else:
            return n if n <= compare_val else '0'


# print(Solution().is_32bit_signed_integer('100')) # True
# print(Solution().is_32bit_signed_integer(str(2**31))) # False
# Solution().reverse(-123)
# Solution().reverse(-120)
# Solution().reverse(-2147483649)
# Solution().reverse(-214748367)
