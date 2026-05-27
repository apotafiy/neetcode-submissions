from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_i = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_i == -1:
                    zero_i = i
                else:
                    return [0 for n in nums]
        prod = reduce(lambda prod, num: prod * (num if num != 0 else 1), nums, 1)
        if zero_i == -1:
            return [prod // num for num in nums]
        else:
            ret = [0] * len(nums)
            ret[zero_i] = prod
            return ret