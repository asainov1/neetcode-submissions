class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ans = []
        def backtrack (index, substring):
            # base case
            print("Entering:", index, substring)
            if index == len(digits): #index = 0
                ans.append(substring)
                return 
            # main part
            current_digit = digits[index] #2
            for letter in phone[current_digit]: #a

                backtrack(index + 1, substring + letter)
            print("Leaving :", index, substring)
        backtrack(0, "")
        return ans
