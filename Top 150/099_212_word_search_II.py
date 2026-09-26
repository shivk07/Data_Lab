class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["$"] = word
        rows, cols = len(board), len(board[0])
        result = []
        def dfs(r, c, parent):
            ch = board[r][c]
            if ch not in parent:
                return
            node = parent[ch]
            word = node.pop("$", None)
            if word is not None:
                result.append(word)
            board[r][c] = "#"
            if r > 0 and board[r - 1][c] != "#":
                dfs(r - 1, c, node)
            if r + 1 < rows and board[r + 1][c] != "#":
                dfs(r + 1, c, node)
            if c > 0 and board[r][c - 1] != "#":
                dfs(r, c - 1, node)
            if c + 1 < cols and board[r][c + 1] != "#":
                dfs(r, c + 1, node)
            board[r][c] = ch
            if not node:
                parent.pop(ch)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie)
        return result