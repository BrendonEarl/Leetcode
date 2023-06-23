class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        x = str(x)
        
        
        return x == x[-1::-1]
    
#next try with pointers
# then use mods to avoid converting to string