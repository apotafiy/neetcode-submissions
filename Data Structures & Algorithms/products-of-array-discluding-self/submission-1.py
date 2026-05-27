from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prod = [1] * len(nums)
        r_prod = [1] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                l_prod[i] = l_prod[i - 1] * nums[i - 1]
        for j in range(len(nums)):
            i = len(nums) - j - 1
            if i != len(nums) - 1:
                r_prod[i] = r_prod[i + 1] * nums[i + 1]
        return [r_prod[i] * l_prod[i] for i in range(len(nums))]