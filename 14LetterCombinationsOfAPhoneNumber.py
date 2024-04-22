from typing import List


class Solution:
    vals = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],

    }
    def letterCombinations(self, digits: str) -> List[str]:
        if (length := len(digits)) == 0:
            return []
        elif length == 1:
            return self.vals[digits[0]]

        test = []
        for d in digits:
            test.append(self.vals[d])

        solve = []
        for a in test[0]:
            for b in test[1]:
                if length > 2:
                    for c in test[2]:
                        if length > 3:
                            for d in test[3]:
                                solve.append("".join([a, b, c, d]))
                        else:
                            solve.append("".join([a, b, c]))
                else:
                    solve.append("".join([a, b]))

        return solve


t = Solution().letterCombinations("237")