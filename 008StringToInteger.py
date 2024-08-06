
class Solution:
    def myAtoi(self, s: str) -> int:
        sm = self.StateMachine()
        return sm.evaluate(s)

    class StateMachine:
        def __init__(self) -> None:
            self.state = 'whitespace'
            self.sign = ''
            self.num = ''

        def evaluate(self, s: str):

            for char in s:
                self.run(char)
                if self.state == 'done':
                    break
            return self.format()

        def run(self, char: str):
            if (ss := self.state) == 'whitespace':
                if not char.isspace():
                    self.state = 'optional_sign'
                    self.run(char)
            elif ss == 'optional_sign':
                self.state = 'gathernums'
                if char in {'-', '+'}:
                    self.sign = char
                else:
                    self.run(char)
            elif ss == 'gathernums':
                if char.isdigit():
                    self.num = self.num + char
                else:
                    self.state = 'done'

        def format(self):
            if not self.num:
                return 0

            return (self.no_leading_zeros(self.num, self.sign))

        def no_leading_zeros(self, n: str, sign: str):

            point = 0
            while n[point] == '0':
                point += 1
                if point == len(n):
                    point -= 1
                    break

            nl = '-' + (n[point:]) if sign == '-' else n[point:]

            return int(self.is_32bit_signed_integer(nl))

        def is_32bit_signed_integer(self, n: str):
            min_value = '-2147483648'
            max_value = '2147483647'
            compare_val = min_value if n[0] == '-' else max_value

            if (nlen := len(n)) < (clen := len(compare_val)):
                return n
            elif nlen > clen:
                return compare_val
            else:
                return n if n <= compare_val else compare_val

# print(Solution().myAtoi("00000-42a1234"))
# print(Solution().myAtoi(" -1123u3761867"))
# print(Solution().myAtoi("words and 987"))
# print(Solution().myAtoi("-91283472332"))

# https://leetcode.com/problems/string-to-integer-atoi
