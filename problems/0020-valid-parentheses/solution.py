class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_i = {"]":"[", ")":"(", "}":"{"}
        for i in s:
            if i in map_i:
                if stack and stack[-1] == map_i[i]: 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False


