class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        len_array = len(arr)    
        i = 0
        
        while i < len_array:
            if arr[i] == 0:
                arr[:] = arr[:i+1]+arr[i:]
                arr[:] = arr[:len_array]
                i += 1
            i += 1
        
        