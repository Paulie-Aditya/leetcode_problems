from collections import Counter
class Solution:
    def countBits(self, n: int) -> List[int]:
        to_return  = []
        for i in range(n+1):
            y = bin(i)
            count = Counter(y)
            to_return.append(count["1"])
        return to_return

