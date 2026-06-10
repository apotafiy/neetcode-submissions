class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        for i in range(len(nums) - 2):
            target = nums[i] * -1
            ret = self.twoSum(nums, i + 1, target)
            for r in ret:
                if r:
                    if nums[i] < r[0]:
                        triplets.add((nums[i], r[0], r[1]))
                    elif nums[i] > r[1]:
                        triplets.add((r[0], r[1], nums[i]))
                    else:
                        triplets.add((r[0], nums[i], r[1]))
        ret = []
        for t in triplets:
            ret.append(list(t))
        return ret

    
    def twoSum(self, nums, start, target) -> set[tuple[int, int]] | None:
        set_ = set()
        ret = set()
        for i in range(start, len(nums)):
            twin = target - nums[i]
            if twin not in set_:
                set_.add(nums[i])
            else:
                ret.add((nums[i] if nums[i] < twin else twin, twin if nums[i] < twin else nums[i]))
        print(f"start={start},target={target},ret={ret}")
        return ret