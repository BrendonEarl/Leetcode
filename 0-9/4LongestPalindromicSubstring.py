"""
    Todo: go through string and in between each character and treat as center of palindrome worst case n^2
    
    stringlen = len(s)
    maxString,maxLen = '', 0
    in = lambda x,y : (x>=0 and x<stringlen) and (y>=0 and y<stringlen)
    eq = lambda x,y : in(x,y) and s[x]==s[y]
    
    for x in range(stringlen*2):
        if x%2:
            l,r,startlen = (int)(floor(x/2)), (int)(ceil(x/2)), 2
        else:
            l,r,startlen= (point:=(int)((x/2))), point, 1
        
        if not eq(l,r): continue
        while l>=0 and r<stringlen:
            if startlen > maxLen:
                maxLen = startlen
                maxString = s[l:r+1] if l!=r else s[l]
            l,r = l-1,r+1
            if not eq(l,r): break 1
                
            
            
        
"""
from math import floor,ceil

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass