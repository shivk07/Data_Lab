from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        target = n * n
        def get_position(square: int) -> tuple[int, int]:
            row_from_bottom = (square - 1) // n
            row = n - 1 - row_from_bottom
            col = (square - 1) % n
            if row_from_bottom % 2 == 1:
                col = n - 1 - col
            return row, col
        queue = deque([(1, 0)])  
        visited = {1}
        while queue:
            curr, rolls = queue.popleft()
            for next_square in range(curr + 1, min(curr + 6, target) + 1):
                r, c = get_position(next_square)
                destination = (
                    board[r][c]
                    if board[r][c] != -1
                    else next_square
                )
                if destination == target:
                    return rolls + 1
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, rolls + 1))
        return -1