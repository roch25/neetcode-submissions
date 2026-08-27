class Solution:
    def isHappy(self, n: int) -> bool:
        done = {}
        
        digits = sum([int(s)**2 for s in list(str(n))])
        while(digits != 1):
            if digits not in done:
                done[digits] = 1
            else:
                return False
            digits = sum([int(s)**2 for s in list(str(digits))])
           
        return True
        