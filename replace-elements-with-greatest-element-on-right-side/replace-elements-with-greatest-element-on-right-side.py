class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) < 1:
            return arr
        
        MAX = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            
            arr[i] = MAX
            
            if MAX < temp:
                MAX = temp
            
        return arr
        