class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]
        for i in range(len(height)):
            if i == 0:
                left_max[i] = height[i]
            else:
                left_max[i] = max(left_max[i - 1], height[i])
        for i in range(len(height) - 1, 0, -1):
            if i == len(height) - 1:
                right_max[i] = height[i]
            else:
                right_max[i] = max(right_max[i + 1], height[i])

        total = 0
        for i in range(len(height)):
            h_val = height[i]
            h_lower = min(left_max[i], right_max[i])
            if h_lower > h_val:
                total += h_lower - h_val
        return total

####
##

###
##
#####