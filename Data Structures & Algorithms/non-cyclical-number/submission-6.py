class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            if n in seen:
                return False
                
            seen.add(n)
            n = sum([int(s)**2 for s in list(str(n))])
           
        return True
        