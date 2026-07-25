from collections import Counter
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # TC: O(N) SC: O(N)
        hashtable = set(wordDict)
        memo = {}
        def backtrack (remaining):
            if len(remaining) == 0:
                return True
            if remaining in memo:
                return memo[remaining]
            tmp = ""
            for ind, w in enumerate(remaining):
                tmp += w
                if tmp in hashtable:
                    if backtrack(remaining[ind+1:]):
                        memo[remaining] = True
                        return True
            memo[remaining] = False
            return False
        return backtrack (s)
        
        
                


