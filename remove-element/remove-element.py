class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # DUMMY WAY SINCE I CANT DO THE EFFICENT ONE
        new_list = []
        for index, value in enumerate(nums):
            if value != val:
                new_list.append(value)
        
        nums[:] = new_list
                
        
        