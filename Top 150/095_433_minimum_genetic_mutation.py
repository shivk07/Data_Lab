from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        queue = deque([(startGene, 0)])
        genes = "ACGT"
        while queue:
            gene, mutations = queue.popleft()
            if gene == endGene:
                return mutations
            for i in range(8):
                for char in genes:
                    if char == gene[i]:
                        continue
                    mutated = gene[:i] + char + gene[i + 1:]
                    if mutated in bank:
                        bank.remove(mutated)
                        queue.append((mutated, mutations + 1))
        return -1