class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        state = "START"
        
        for index ,value in enumerate(arr):
            if state == "START":
                if value < arr[index+1]:
                    state = "UP"
                else:
                    return False
            elif state == "UP":
                if value < arr[index+1]:
                    pass
                elif value == arr[index+1]:
                    return False
                else:
                    state = "DOWN"
            elif state == "DOWN":
                if value < arr[index+1]:
                    return False
                elif value == arr[index+1]:
                    return False
                else:
                    state = "DOWN"
            
                    
            if index+1 == len(arr)-1:
                if state == "UP":
                    return False
                break
                
        
        
        return True #if state != "UP" else False
                
            
    
        