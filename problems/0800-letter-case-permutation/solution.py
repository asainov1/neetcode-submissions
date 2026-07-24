class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack (curr, index):
            print (curr)
            if len(curr) == len(s):
                ans.append(''.join(curr))
                return 
            c = s[index]
            if c.isnumeric():
                backtrack(curr + [c], index + 1)
            else:
                backtrack(curr + [c.lower()], index + 1)
                backtrack(curr + [c.upper()], index + 1)
        backtrack([],0)
        return ans
