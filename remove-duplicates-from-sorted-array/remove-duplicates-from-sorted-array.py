class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for index,value in enumerate(nums):
            if nums[j] != value:
                
                j += 1
                nums[j] = value
                
        return j+1