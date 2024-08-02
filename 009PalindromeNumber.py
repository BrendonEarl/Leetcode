class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        counter, t = -1, x
        while t:
            t = t//10
            counter += 1

        w, t = 0, x
        for i in range(counter, -1, -1):
            w += (t % 10)*(10**i)
            t = t//10

        return w == x


Solution().isPalindrome(x=666)

# https://leetcode.com/problems/palindrome-number

