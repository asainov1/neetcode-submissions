from collections import deque
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        q = deque()
        for num in operations:
            if num.isdigit():
                q.append(num)
            elif "-" in num:
                q.append(int(num))
            elif num == "C":
                q.pop()
            elif num == "D":
                last_num = q.pop()
                q.append(last_num)
                new_num = 2 * int(last_num)
                q.append(new_num)
            elif num == "+":
                q.append(int(q[-1]) + int(q[-2]))
        print (q)
        return sum([int(num) for num in q])

