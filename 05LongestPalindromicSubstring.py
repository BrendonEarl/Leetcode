"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
              
"""

from math import floor,ceil

class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        stringlen = len(s)
        maxString,maxLen = '', 0
        
        in_bounds = lambda x,y : (x>=0 and x<stringlen) and (y>=0 and y<stringlen)
        eq = lambda x,y : in_bounds(x,y) and s[x]==s[y]
        
        for index in range(stringlen*2):
            if index%2:
                l, r, startlen = (int)(floor(index/2)), (int)(ceil(index/2)), 2
            else:
                l, r, startlen= (point:=(int)((index/2))), point, 1
            
            if not eq(l,r):
                continue
            
            while l>=0 and r<stringlen:
                if startlen > maxLen:
                    maxLen = startlen
                    maxString = s[l:r+1] if l!=r else s[l]
                l,r = l-1,r+1
                
                if not eq(l,r):
                    break
                startlen += 2
        
        # print(maxString)
        return maxString
    
# Solution().longestPalindrome(s = "babad")
# print('-------------')
# Solution().longestPalindrome(s = "cbbaabbc")        