class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        def backtrack(index):
            tmp = ""
            number = 0
            while index < len(s):
                if s[index].isalpha():
                    tmp += s[index]
                    index += 1
         
                elif s[index].isdigit():
                    number = number * 10 + int(s[index])
                    index += 1
                elif s[index] == "[":
                    decoded, index = backtrack(index + 1)
                    tmp += number * decoded
                    number = 0
                    index += 1
                else:
                    return tmp, index
            return tmp, index
        ans, _ = backtrack(0)
        return ans
