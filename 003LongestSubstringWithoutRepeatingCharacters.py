

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
