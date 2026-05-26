import heapq as hq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            hq.heappush(heap,-1 * n)
        for _ in range(k - 1):
            hq.heappop(heap)
        return -1 * hq.heappop(heap)