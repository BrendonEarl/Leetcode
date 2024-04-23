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

        print(self.letterCombinationsHelper(test, length - 1))

    def letterCombinationsHelper(self, test: List[str], index) -> List[str]:
        if index < 0:
            return ['']
        return [(y + z) for y in (self.letterCombinationsHelper(test, index - 1)) for z in test[index]]


t = Solution().letterCombinations("237")
