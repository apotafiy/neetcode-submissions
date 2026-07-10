class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # [1,7,2,5,4,7,3,6]
        # [1,7,7,7,7,7,7,7]
        # [7,7,7,7,7,7,6,6]
        max_ = 0
        for i in range(len(heights) - 1):
            for j in range(1, len(heights)):
                # print(f"i={i}, j={j}")
                h = (j - i) * min(heights[i], heights[j])
                max_ = max(max_, h)
        return max_