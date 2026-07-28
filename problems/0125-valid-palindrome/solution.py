class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        TC O(N) SC O(1)
        right = 0
        s = s.strip()
        while left < len(s): 
            # base case 
            if s[left].lower() != s[right].lower():
                return False
            elif s[left].isalnum():
                left += 1
            elif s[right].isalnum():
                right -= 1
        return True

        x.isalnum()
        s = "Aman,aplan,acanal:Panama"
                         ^^

        """
        
        left = 0
        s = "".join(s.split())
        right = len(s) - 1
        print (s)
        while left < right:
            # base case 
            if s[left].lower() != s[right].lower() and s[left].isalnum() and s[right].isalnum():
                return False
            elif not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                left += 1
                right -= 1
                print (s[left], left, s[right], right)
        return True
