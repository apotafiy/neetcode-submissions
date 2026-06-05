import heapq as hq

class Pair:
    def __init__(self, priority: float, coords: List[int]):
        self.priority: float = priority
        self.coords: tuple[int, int] = coords
    
    def __lt__(self, other):
        return self.priority < other.priority

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = list(map(lambda point: Pair(((point[0] ** 2) +(point[1] ** 2)) ** 0.5, point), points))
        hq.heapify(heap)
        vals = []
        for _ in range(k):
            vals.append(hq.heappop(heap).coords)
        return vals