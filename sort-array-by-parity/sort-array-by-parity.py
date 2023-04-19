class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        first_index = 0
        last_index = len(nums)-1
        
        while first_index < last_index:
            if nums[first_index] %2 != 0:
                nums.append(nums.pop(first_index))
                last_index -= 1
                
            
            if nums[first_index] %2 == 0:
                first_index += 1
        return nums