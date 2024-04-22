class Solution:
    def __init__(self) -> None:
        self.symbols = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
    }
    def romanToInt(self, s: str) -> int:
        check = lambda char: self.symbols[char]
        slen, tot = len(s)-1, 0
        for idx, ch in enumerate(s):
            val = check(ch)
            if idx < slen and val < check(s[idx + 1]):
                tot -= val
            else:
                tot += val
        return tot

        