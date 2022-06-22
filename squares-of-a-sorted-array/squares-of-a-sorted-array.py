class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        returnList = []
        leftPointer, rightPointer = 0,len(nums)-1
        
        while leftPointer <= rightPointer:
            # if :
            #     returnList.insert(0,nums[leftPointer] ** 2)
            #     break
                
            if nums[leftPointer] ** 2 <= nums[rightPointer] ** 2:
                returnList.insert(0,nums[rightPointer] ** 2)
                rightPointer -= 1
            else:
                returnList.insert(0,nums[leftPointer] ** 2)
                leftPointer += 1
            
            
            
            
        
        return returnList
            
            
        
        
            
            
        