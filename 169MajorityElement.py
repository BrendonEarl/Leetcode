from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        done = []

        for num in nums:
            if (num not in done) and (nums.count(num) > len(nums)/2):
                return num
            done.append(num)

    #todo: hash table

# https://leetcode.com/problems/balanced-binary-tree
