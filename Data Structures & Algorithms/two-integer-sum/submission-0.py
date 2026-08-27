class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, number in enumerate(nums):
            new_list = nums[:index] + nums[index+1:]
            print(target - number)
            if (target - number) in new_list:
                return [index, new_list.index(target - number) + 1]
            
        
        return [0, 0]