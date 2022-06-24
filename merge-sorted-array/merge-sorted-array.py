class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(len(nums1)-1,len(nums2)-1,m,n)
        
        
        nums1_index, nums2_index = 0,0
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        
        nums1 += nums2
        
        nums1[:] = self.sort(nums1)
                
    def sort(self, nums1: List[int]):
        if len(nums1) <= 1:
            return nums1
        
        pivot = random.choice(nums1)
        
        lt = [v for v in nums1 if v < pivot]
        eq = [v for v in nums1 if v == pivot]
        rt = [v for v in nums1 if v > pivot]
        
        return self.sort(lt)+eq+self.sort(rt)
        
        
        
        
        