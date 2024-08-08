from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        inBounds = lambda r, c: (r >= 0) and (r < rows) and (c >= 0) and (c < cols)
        result, i = [], 0
        rn, cn = rStart, cStart

        if inBounds(rn, cn):
            result.append([rn, cn])

        while len(result) < (rows * cols):

            i += 1
            for j in range(i):
                cn += 1
                if inBounds(rn, cn):
                    result.append([rn, cn])

            for k in range(i):
                rn += 1
                if inBounds(rn, cn):
                    result.append([rn, cn])
            i += 1
            for l in range(i):
                cn -= 1
                if inBounds(rn, cn):
                    result.append([rn, cn])

            for m in range(i):
                rn -= 1
                if inBounds(rn, cn):
                    result.append([rn, cn])

        return result


Solution().spiralMatrixIII(rows=5, cols=6, rStart=1, cStart=4)

# todo efficiency
# https://leetcode.com/problems/spiral-matrix-iii/
