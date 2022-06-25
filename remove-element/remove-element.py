class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_list = []
        for index, value in enumerate(nums):
            if value != val:
                print(value,val)
                new_list.append(value)
        
        nums[:] = new_list
                
        
        