from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            if reduce(lambda x, y: x ^ y, nums[:index] + nums[index+1:], 0) == 0:
                return num
        