class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (right + left) // 2
            arr = matrix[mid]
            if arr[0] <= target and target <= arr[-1]:
                return self.bs(arr, target)
            elif arr[-1] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        
    def bs(self, nums: List[int], target: int):
        if len(nums) == 0: return False
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            num = nums[mid]
            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                 right = mid - 1
        return False