


class Solution:
    vals = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    def isValid(self, s: str) -> bool:
        if (l := len(s)) == 0: return True
        if l % 2: return False

        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif len(stack) > 0 and self.vals[stack.pop()] == c:
                continue
            else:
                return False
        return not len(stack)


z = Solution().isValid("{([]{}){}{{}}}")
print(z)
