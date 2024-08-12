
class Solution:

    vals = [2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    def hammingWeight(self, n: int) -> int:
        response = 0
        for v in self.vals:
            if n >= v:
                response += 1
                n -= v
        return response

Solution().hammingWeight(2147483645)
# https://leetcode.com/problems/number-of-1-bits/
