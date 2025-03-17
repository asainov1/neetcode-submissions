class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_1 = deque()
        stack_2 = deque()
        l = 0
        for i in range(len(s)):
            if s[i] == '#':
                if stack_1: 
                    stack_1.pop()
            else: stack_1.append(s[i])
        for j in range(len(t)):
            if t[j] == '#':
                if stack_2: 
                    stack_2.pop()
            else: stack_2.append(t[j])
        if stack_1 == stack_2:
            return True
        return False
