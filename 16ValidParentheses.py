"""
( - 40
) - 41
[ - 91
] - 93
{ - 123
} - 125
"""


class Solution:
    vals = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    bs = vals.keys()
    es = vals.values()

    def isValid(self, s: str) -> bool:
        if (l := len(s)) == 0: return True
        if l % 2: return False

        start_val, count, rstrings, start_pointer = s[0], 1, [], 0
        if start_val not in self.bs: return False

        for i in range(1, l):
            test = s[i]
            if not count:
                count += 1
                start_val = test

                if start_val not in self.bs: return False
                rstrings.append(s[start_pointer + 1:i - 1])
                start_pointer = i
                continue

            if test == start_val:
                count += 1
            if test == self.vals[start_val]:
                count -= 1

        if not count:
            count += 1
            if test in self.bs: return False
            rstrings.append(s[start_pointer + 1: l - 1])
        else:
            return False

        return all([self.isValid(r) for r in rstrings])

#todo optimize with stack
z = Solution().isValid("{([]{}){}{{}}{}")
print(z)
