class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return None
        nums.sort()
        # print(nums)
        # [-4,-1,-1,0,1,2]
        # [-3,-2,-1,0,1,2,3]
        triplets = []
        i = 0
        while i < len(nums) - 2:
            # print(f"i={i}")
            num = nums[i]
            triplets.extend(self.twoSum(nums,i + 1, num * -1))
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return triplets

    
    def twoSum(self, nums, start, target) -> list[list[int, int]]:
        pairs = []
        end = len(nums) - 1
        while start < end:
            sum_ = nums[start] + nums[end]
            # print(f"target={target},start={nums[start]},end={nums[end]}")
            if sum_ == target:
                pairs.append([target * -1, nums[start], nums[end]])
                # print(f"pair={[target * -1, nums[start], nums[end]]}")
                while start < len(nums) - 1 and nums[start] == nums[start + 1]:
                    start += 1
                while end > 0 and nums[end] == nums[end - 1]:
                    end -= 1
            if sum_ < target or sum_ == target:
                start += 1
            if sum_ > target or sum_ == target:
                end -= 1
            
        return pairs