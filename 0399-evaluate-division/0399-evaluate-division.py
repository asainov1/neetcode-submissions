from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(current, target, visited):
            if current == target:
                return 1.0

            visited.add(current)

            for neighbor, weight in graph[current]:
                if neighbor in visited:
                    continue

                result = dfs(neighbor, target, visited)
                if result != -1.0:
                    return weight * result

            return -1.0

        answers = []

        for start, target in queries:
            if start not in graph or target not in graph:
                answers.append(-1.0)
            else:
                answers.append(dfs(start, target, set()))

        return answers