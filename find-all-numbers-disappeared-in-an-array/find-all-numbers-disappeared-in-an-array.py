class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_num = set(list(range(1,len(nums)+1))).difference(set(nums))
        return list(new_num)
        