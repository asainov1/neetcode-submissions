class Solution:

    def dfs(self, x, y, val):
        if x == y:
            return val

        # Уже были в x во время этого поиска — не ходим по кругу
        if self.states[x] == 1:
            return -1.0

        self.states[x] = 1

        for next_node, weight in self.edges.get(x, []):
            result = self.dfs(next_node, y, val * weight)

            if result != -1.0:
                return result

        return -1.0

    def calcEquation(self, equations, values, queries):
        self.edges = {}

        for (x, y), value in zip(equations, values):
            self.edges.setdefault(x, []).append((y, value))
            self.edges.setdefault(y, []).append((x, 1 / value))

        self.result = []

        for x, y in queries:
            if x not in self.edges or y not in self.edges:
                self.result.append(-1.0)
                continue

            # Новый поиск — новые состояния узлов
            self.states = {node: 0 for node in self.edges}

            val = self.dfs(x, y, 1.0)
            self.result.append(val)

        return self.result