import random

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            nums.insert(0,nums.pop()**2)
            return nums
        
        first_index,last_index = 0,len(nums)-1
        
        while first_index <= last_index:
            if nums[first_index]**2 >= nums[last_index]**2:
                nums.insert(last_index,nums.pop(first_index)**2)
                last_index -= 1
            elif nums[first_index]**2 < nums[last_index]**2:
                nums.insert(last_index,nums.pop(last_index)**2)
                last_index -= 1
                
        return nums
            
        
        
            
            
        