class Solution:
    def decodeString(self, s: str) -> str:
        stack, curnum, curstring = [],0,''
        for c in s:
            if c == '[':
                stack.append(curstring) # LIFO
                stack.append(curnum)  # LIFO 
                curstring = ''
                curnum = 0
            elif c == ']':
                num = stack.pop()  # LIFO
                prevstring = stack.pop() # LIFO
                curstring = prevstring + num * curstring
            elif c.isdigit():
                curnum = curnum * 10 + int(c)
            else:
                curstring += c
        return curstring

