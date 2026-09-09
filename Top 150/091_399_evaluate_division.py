from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))
        def dfs(start, target, visited):
            if start == target:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start]:
                if neighbor not in visited:
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