from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        refused = 0
        q = deque(students)
        left = 0
        while q and left < len(sandwiches):
            if sandwiches[left] == q[0]:
                q.popleft()
                refused = 0
                left += 1
            else:
                first = q.popleft()
                q.append(first)
                refused += 1

            if refused == len(q):
                return len(q)
        return refused
                
        
