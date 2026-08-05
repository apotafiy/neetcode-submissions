class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(0, len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                return i + 1
        return nums[-1] + 1