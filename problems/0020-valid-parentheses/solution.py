class Solution:
    def isValid(self, s: str) -> bool:
        opens = {")":"(", "]":"[","}":"{"}
        stack = []

        for l in s:
            if l not in opens:
                stack.append(l)
            else:
                if not stack:
                    return False
                pops = stack.pop()
                if pops != opens[l]:
                    return False      
        return not stack

