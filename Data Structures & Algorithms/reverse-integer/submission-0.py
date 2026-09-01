class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        y = abs(x)
        for i in range(len(str(y))):
            sum += int(str(y)[i]) * 10**(int(i))

        if sum < -(1 << 31) or sum > (1 << 31) - 1:
            return 0
        return sum if x > 0 else -sum

        