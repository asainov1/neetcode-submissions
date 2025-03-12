class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, dst: int) -> bool:

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()

        def dfs(i):
            seen.add(i)
            for nei_node in graph[i]:
                if nei_node not in seen:
                    dfs(nei_node)
        
        dfs(source)
        
        return dst in seen

        
