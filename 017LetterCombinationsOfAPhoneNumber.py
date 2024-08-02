from typing import List


class Solution:

    keyPadDict = {
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
            return self.keyPadDict[digits[0]]

        letters = []
        for d in digits:
            letters.append(self.keyPadDict[d])

        return self.letterCombinationsHelper(letters, length - 1)

    def letterCombinationsHelper(self, letters: List[str], index) -> List[str]:
        if index < 0:
            return ['']
        return [(y + z) for y in (self.letterCombinationsHelper(letters, index - 1)) for z in letters[index]]


t = Solution().letterCombinations("237")
print(t)

# https://leetcode.com/problems/letter-combinations-of-a-phone-number
