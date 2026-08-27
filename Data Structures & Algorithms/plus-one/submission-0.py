class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(str(i) for i in digits))
        return  list(map(int, str(~number * -1))) 
        