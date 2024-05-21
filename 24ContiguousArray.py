from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nlen = len(nums)
        starting_length = nlen - 1 if nlen % 2 else nlen

        if nlen < 2:
            return 0
        if nlen == 2 or nlen == 3:
            return 2 if (nums.count(0) == 1 or nums.count(1) == 1) else 0

        check = []
        z = 0
        while nums:
            c = nums.pop()
            add = c if c else -1
            check.append(0)
            check = [y + add for y in check]
            #todo check odd/even vals for zero. len-index * 2 > previous
            z+=1
            print(check)







t = Solution().findMaxLength([0,1,1,0,1,1,1,0])
print(t)


print([1,1,1,0][1::2])