class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        counter, t = -1, x
        while (t):
            t = t//10
            counter += 1
        
        w, t = 0, x
        for i in range(counter,-1,-1):
            w += (t%10)*(10**i)
            t = t//10
            
        return w==x
        
        
"""
def isPalindrome(self, x: int) -> bool:
    if x<0:
        return False
    x = str(x)
    return x == x[-1::-1]
"""

#next try with pointers
# then use mods to avoid converting to string
Solution().isPalindrome(x = 666)