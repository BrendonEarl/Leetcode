from typing import List


class TwoSum:

    def __init__(self, nums, target) -> None:
        print(self.twoSum(nums, target))

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for x in range(0, length):
            for y in range(x, length):
                if (x != y) and (nums[x] + nums[y] == target):
                    return [x, y]
        return []


TwoSum(nums=[3, 2, 4], target=6)
# https://leetcode.com/problems/two-sum
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

