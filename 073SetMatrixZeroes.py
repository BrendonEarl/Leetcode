from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zr, zc = [], []
        # [print(x) for x in matrix]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if not val:
                    zr.append(r)
                    zc.append(c)
        matrix[:] = [
            [(0 if ((c in zc) or (r in zr)) else val) for c, val in enumerate(row)] for r, row in enumerate(matrix)
        ]
        # print(matrix)


# https://leetcode.com/problems/set-matrix-zeroes/

Solution().setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
