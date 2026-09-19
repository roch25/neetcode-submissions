class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        print(n)
        for i in range(n):
            print(i, "i", nums[i], ".", i ^ nums[i])
            xorr ^= i ^ nums[i]
            print(xorr)
        return xorr