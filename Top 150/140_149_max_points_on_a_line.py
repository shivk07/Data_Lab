from collections import defaultdict
from math import gcd
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        result = 0
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                slopes[(dy, dx)] += 1
            if slopes:
                result = max(result, max(slopes.values()) + 1)
        return result