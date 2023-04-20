import random
class Solution:
    def sort(self,heights: List[int]) -> List[int]:
        if len(heights) <= 1:
            return heights
        
        pivote = random.choice(heights)
        
        left = [i for i in heights if i < pivote]
        middle = [i for i in heights if i == pivote]
        right = [i for i in heights if i > pivote]
        
        return self.sort(left)+middle+self.sort(right)
    
    
    def heightChecker(self, heights: List[int]) -> int:
        return [i==j for i,j in zip(self.sort(heights),heights)].count(False)
    