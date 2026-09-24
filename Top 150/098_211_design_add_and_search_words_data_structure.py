class WordDictionary:
    def __init__(self):
        self.root = {}
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = True  
    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return "#" in node
            char = word[index]
            if char == ".":
                for key, child in node.items():
                    if key != "#" and dfs(index + 1, child):
                        return True
                return False
            if char not in node:
                return False
            return dfs(index + 1, node[char])
        return dfs(0, self.root)