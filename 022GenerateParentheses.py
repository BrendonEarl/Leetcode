from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        answer, answers = ("(" * n + ")" * n), [("(" * n + ")" * n)]

        while answer[:2] == "((":

            for i, c in enumerate(answer):
                if c == ")":
                    l, c, r = answer[:i - 1], answer[i - 1:i + 1], answer[i + 1:],
                    break
            print([l, c, r])
            while l:
                r = l[-1] + r
                l = l[:-1]
                answer2 = l + c + r
                if answer2 not in answers:
                    answers.append(answer2)

            while r:

                l = l + r[0]
                r = r[1:]
                answer = l + c + r
                if answer not in answers:
                    answers.append(answer)

        return answers


print("string"[:-1])
t = Solution().generateParenthesis(4)
print(t)
print(q := ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()",
            "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"])
# todo

for e in q:
    if e not in t:
        print(e)

# https://leetcode.com/problems/generate-parentheses
