class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_ = nums[0]
        cur_sum = 0
        i = 0
        j = 0
        while j < len(nums):
            while cur_sum >= 0 and j < len(nums):
                cur_sum += nums[j]
                max_ = max(max_, cur_sum)
                j += 1
            i = j
            cur_sum = 0
        return max_