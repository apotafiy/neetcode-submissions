class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,7,1,2]
        # [6,7,1,2,3,4,5]
        if len(nums) == 1:
            return nums[0]
        
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else: return nums[m]
        return nums[l]
