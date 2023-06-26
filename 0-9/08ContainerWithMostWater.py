from typing import List
import time


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        def check(x, y): return min(height[x], height[y])*abs(y-x)

        lgst = 0

        while l < r:
            lgst = max(lgst, check(l, r))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return lgst

Solution().maxArea(height = [1,8,6,2,5,4,8,3,7])
