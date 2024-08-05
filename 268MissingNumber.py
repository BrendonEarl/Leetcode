from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        t = [0 for x in range(n + 1)]

        for y in nums:
            t[y] += 1

        for i, z in enumerate(t):
            if not z:
                return i


s = Solution().missingNumber([9,6,4,2,3,5,7,0,1])
print(s)