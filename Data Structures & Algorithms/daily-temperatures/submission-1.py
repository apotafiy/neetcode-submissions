class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            val = temperatures[i]
            while stack and val > stack[-1][1]:
                pair = stack.pop()
                index = pair[0]
                value = pair[1]
                res[index] = i - index
            stack.append([i, val])
        return res