class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return 
        
        first_index = 0
        last_index = len(nums)-1
        
        while first_index < last_index:
            if nums[first_index] == 0:
                nums.append(nums.pop(first_index))
                last_index -= 1
            
            if nums[first_index] != 0:
                first_index += 1
            