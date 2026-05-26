class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i, num in enumerate(nums):
            match = target - num
            if match in vals:
                return [vals.get(match), i]
            if num not in vals:
                vals[num] = i