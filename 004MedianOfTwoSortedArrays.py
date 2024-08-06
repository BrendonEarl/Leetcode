from typing import List
from math import floor


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if isOdd := bool((tot := (len(nums1) + len(nums2))) % 2):
            goal_index = [int(floor(tot / 2))]
        else:
            goal_index = [half := int(tot / 2) - 1, half + 1]

        one, two = 0, 0
        len1, len2 = len(nums1), len(nums2)

        if not len1 or not len2:
            nonZero = nums1 if len1 > 0 else nums2
            return nonZero[goal_index[0]] if isOdd else ((nonZero[goal_index[0]] + nonZero[goal_index[1]]) / 2)

        test = []
        for _ in range(goal_index[-1] + 1):
            if two == len2 or (one <= len1 - 1 and nums1[one] < nums2[two]):
                test.append(nums1[one])
                one += 1
            else:
                test.append(nums2[two])
                two += 1

        return (float(test[-1])) if isOdd else (sum(test[-2::]) / 2)


# Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4])
# print('--------------------------------------------')
# Solution().findMedianSortedArrays(nums1=[1, 3], nums2=[2])
# print('--------------------------------------------')
# Solution().findMedianSortedArrays(nums1=[1, 3,4,5,6], nums2=[2])
# print('--------------------------------------------')
# Solution().findMedianSortedArrays(nums1=[1,1,1,1,1,1,1,1,1,1,1], nums2=[2])
# print('--------------------------------------------')
# Solution().findMedianSortedArrays(nums1=[1,1,1,1,1,1,1,1,1,1], nums2=[2])

# https://leetcode.com/problems/median-of-two-sorted-arrays
