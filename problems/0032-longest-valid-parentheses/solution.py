class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = ['0'] * len(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if stack:
                    l[stack.pop()] = '1'
                    l[i] = '1'

        return (max(len(i) for i in "".join(l).split('0')))

