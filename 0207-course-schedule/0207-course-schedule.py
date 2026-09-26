class Solution:
    def dfs(self, node):
        # hold states 0 -  unprocessed , 1 - in progress 2 - passed
        if self.state[node] == 2:
            return True
        if self.state[node] == 1:
            return False
        self.state[node] = 1
        for edge in self.edges.get(node, []):
            if not self.dfs(edge):
                return False
        self.state[node] = 2
        return True
    
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        graph problem 
        DFS/BFS - any appropriate
        DFS search TC: O(mn) SC(mn)
        """
        #directed graph -  build adjacency list
        #1. creating adjacency list
        self.edges = {}
        self.state = [0] * numCourses
        for course, prereq in prerequisites:
            if course not in self.edges:
                self.edges[course] = []
            self.edges[course].append(prereq)
        
        for i in range(0, numCourses):
            if not self.dfs(i):
                return False

        
        return True


       