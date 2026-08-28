class Solution:
    def countBits(self, n: int) -> List[int]:
        return [sum([int(j) for j in str(bin(i)[2:])]) for i in range(n+1)] 
        