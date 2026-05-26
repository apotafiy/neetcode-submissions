class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # "0 1 2 3 4"
        while left <= right:
            middle = self.mid(left, right)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1

    def mid(self, left: int, right: int):
        return int((left + right)/2)