class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        weakest = []
        n = len(mat)

        check = {}

        for i in range(n):
            check.update({i:mat[i].count(1)})
        
        for y in sorted(check.items(), key=lambda x:x[1]) [:k]:
            weakest.append(y[0])
        return weakest

