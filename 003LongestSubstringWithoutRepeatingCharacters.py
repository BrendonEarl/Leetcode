"""
    Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        max, longest, longest_length = len(s), [], 0
        for index, _ in enumerate(s):
            chars = []
            ll = 0
            spoint = index
            while True:
                if spoint >= max:
                    if ll > longest_length:
                        longest_length = ll
                        longest = chars
                    break
                if (a := s[spoint]) not in chars:
                    chars.append(a)
                    ll += 1
                    spoint += 1
                else:
                    if ll > longest_length:
                        longest_length = ll
                        longest = chars
                    break
        print(f'chars: {longest} \n length: {longest_length}')
        return longest_length

    def lengthOfLongestSubstringSpeed(self, s: str) -> int:
        longest_length, spoint, epoint, longest = 0, 0, 0, []

        visited = {}
        for epoint, char in enumerate(s):
            if char in visited and (new_spoint := visited[char] + 1) > spoint:
                spoint = new_spoint
            else:
                if (new_longest_length := epoint - spoint + 1) > longest_length:
                    longest_length = new_longest_length
                    longest = s[spoint:epoint + 1]

            visited[char] = epoint
        print(f'chars: {longest} \n length: {longest_length}')
        return longest_length


Solution().lengthOfLongestSubstringSpeed("pwwkew")

# https://leetcode.com/problems/longest-substring-without-repeating-characters
