from typing import List


class Solution:
    visited = []
    def orangesRotting(self, grid: List[List[int]]) -> int:
        [print(x) for x in grid]
        #no 1s
        if all([(1 not in x) for x in grid]): return 0
        #islands

        for row, arr in enumerate(grid):
            for col,val in enumerate(arr):
                self.visited.append((row,col))
        print(self.visited)



y = Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
# z = Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
# a = Solution().orangesRotting([[0,2],[0,2]])
# print(a) todo

# https://leetcode.com/problems/rotting-oranges
