from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if (length := len(nums)) < 3:
            return []
        answers = []
        for z in range(length-2):
            target = 0 - nums[z]

            for x in range(z+1, length-1):
                for y in range(x+1, length):
                    if nums[x]+nums[y] == target:
                        if (zxy := sorted([nums[z], nums[x], nums[y]])) not in answers:
                            answers.append(zxy)
        return answers

Solution().threeSum([-1,0,1,2,-1,-4])