class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(row, col, size):
            val = grid[row][col]
            same = True
            for i in range(row, row + size):
                for j in range(col, col + size):
                    if grid[i][j] != val:
                        same = False
                        break
                if not same:
                    break
            if same:
                return Node(val == 1, True)
            half = size // 2
            topLeft = dfs(row, col, half)
            topRight = dfs(row, col + half, half)
            bottomLeft = dfs(row + half, col, half)
            bottomRight = dfs(row + half, col + half, half)
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        return dfs(0, 0, len(grid))