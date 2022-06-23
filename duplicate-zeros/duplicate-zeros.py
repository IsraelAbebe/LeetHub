class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        """
        Runtime: 1087 ms
        Memory Usage: 14.9 MB
        """
        len_array = len(arr)    
        i = 0
        
        
        while i < len_array:
            if arr[i] == 0:
                arr.insert(i,0)
                arr.pop()
                i += 1
            i += 1
        
        
        
        
#         FIRST ATTEMPT
#         Runtime: 1087 ms
#         Memory Usage: 14.9 MB  


#         len_array = len(arr)    
#         i = 0
        
#         while i < len_array:
#             if arr[i] == 0:
#                 arr[:] = arr[:i+1]+arr[i:]
#                 arr[:] = arr[:len_array]
#                 i += 1
#             i += 1
        
        