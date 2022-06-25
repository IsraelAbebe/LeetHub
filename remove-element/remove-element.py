class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        custom_index = 0
        for index, value in enumerate(nums):
            if value != val:
                nums[custom_index] = value
                custom_index += 1
                
        return custom_index
                
            
                
    
                
        
        