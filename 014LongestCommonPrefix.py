from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for _, s in enumerate(strs):
            if s == ans:
                continue
            no_eq = min((slen := len(s)), (alen := len(ans)))
            small = min(slen, alen)
            for i in range(small):
                if s[i] != ans[i]:
                    no_eq = i
                    break
            ans = ans[0:no_eq]
        return ans


print(Solution().longestCommonPrefix(["ag", "a"]))

# https://leetcode.com/problems/longest-common-prefix
