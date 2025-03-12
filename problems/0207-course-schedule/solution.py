class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        was = [0] * numCourses
        
        for course, p in prerequisites:
            graph[course].append(p)
        
        def find_cycle (v):
            if was[v] == 1: # already visitting, cycle detected 
                return True
            if was[v] == 2: # already checked (normal path?)
                return False 

            was[v] = 1 # mark as visitting 

            for to in graph[v]:
                if find_cycle(to):
                    return True # Cycle
            
            was[v] = 2 # mark as fully processed
            return False

        for course in range(numCourses):
            if was[course] == 0: # not visitted
                if find_cycle(course): # check
                    return False
        return True


  
