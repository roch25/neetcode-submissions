class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            stones.sort()
            m1 = stones.pop(len(stones)-1)
            m2 = stones.pop(len(stones)-1)
            if m1 != m2:
                stones.append(m1 - m2)
            
        return stones[0] if len(stones) else  0