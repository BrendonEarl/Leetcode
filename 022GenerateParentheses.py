from traceback import print_stack
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        answers = []
        answers.append('('* n + ')' * n)
        if n == 1: return answers

        answers.append('()'*n)
        if n == 2: return answers

        for i in range(n-1,1,-1):
            print(n-i)
            for j in range(i-1,-1,-1):
                spaces = ['' for _ in range(i+1)]
                spaces[j] = '('*(n-i)
                spaces[j+1] = ')'*(n-i)
                print(spaces)
                # self.print_stack(spaces)

        return answers

    def print_stack(self,arr):
        print('()'.join(arr))



# print("string"[:-1])
t = Solution().generateParenthesis(6)
print('answer')
print(t)
# print(t)
print(q := ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"])
# todo
for e in q:
    print(e.replace('(','L').replace(')','R'))
# for e in q:
#     if e not in t:
#         print(e)

# https://leetcode.com/problems/generate-parentheses
