class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l, place = 0, 0
        stack = []
        for ind, char in enumerate(s):
            if l < len(spaces) and ind == spaces[place]:
                stack.append(' ')
                place += 1
                l += 1
                stack.append(char)
            else:
                stack.append(char)
        return ("".join(stack))

