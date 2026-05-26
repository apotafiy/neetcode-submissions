import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_h = []
        for stone in stones:
            heapq.heappush(max_h, -1 * stone)        
        
        while len(max_h) > 1:
            max_1 = -1 * heapq.heappop(max_h)
            max_2 = -1 * heapq.heappop(max_h)

            new_stone = None
            if max_1 != max_2:
                heapq.heappush(max_h, -1 * (max_1 - max_2))
        return 0 if len(max_h) < 1 else max_h[0] * -1