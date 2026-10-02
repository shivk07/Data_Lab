class Solution:
    def checkPermutation(self, a: list[int], b: list[int]) -> bool:
        if len(a) != len(b):
            return False
        
        fq = {}
        
        for x in a:
            if x in fq:
                fq[x] += 1
            else:
                fq[x] = 1
        
        for x in b:
            if x not in fq:
                return False
            
            fq[x] -= 1
            
            if fq[x] == 0:
                del fq[x]
        
        return len(fq) == 0