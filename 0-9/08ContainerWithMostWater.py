from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        check = lambda x,y : min(height[x],height[y])*abs(y-x)
        lgst = 0
        while l < r:
            print(f'checking {l,r} = {check(l,r)}')
            if( new:=check(l,r)) > lgst:
                print(f'{new}')
                lgst = new
            l, r = l+1, r-1
            print(l,r)
        print(lgst)
        return(lgst)

Solution().maxArea(height = [1,8,6,2,5,4,8,3,7])