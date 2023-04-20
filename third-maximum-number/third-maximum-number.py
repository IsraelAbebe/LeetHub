import random

class Solution:
    def modefied_sort(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums
        
        pivote = random.choice(nums)
        
        left,right,middle= [],[],[]
        [left.append(i) for i in nums if i < pivote and i not in left ]
        [middle.append(i) for i in nums if i == pivote and i not in middle ]
        [right.append(i) for i in nums if i > pivote and i not in right ]
        
        return self.modefied_sort(left)+middle+self.modefied_sort(right)
    def thirdMax(self, nums: List[int]) -> int:
        sorted_list = self.modefied_sort(nums)
        return sorted_list[-3] if len(sorted_list) >=3 else sorted_list[-1]
                
        