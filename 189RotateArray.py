from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[0:-k]


Solution().rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)

# https://leetcode.com/problems/rotate-array
