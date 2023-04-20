class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) < 1:
            return len(nums)-1
        
        if len(nums) == 1:
            return len(nums) if nums[0] != val else 0
                
            
        
        left = [i for i in nums if i != val ]
        right = [i for i in nums if i == val]
        
        nums[:] = left+right
        # print(nums, left,right,len(left))
        return len(left)
        
                
            
                
    
                
        
        