class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        attempts,ind = 0, 0
        students = deque(students)
        sandwiches = deque(sandwiches)


        while students and attempts < len(students):
            if students[ind] == sandwiches[ind]: 
                students.popleft()
                sandwiches.popleft()
                attempts = 0
            else:
                students.append(students.popleft())
                attempts += 1
        return len(students)

            

