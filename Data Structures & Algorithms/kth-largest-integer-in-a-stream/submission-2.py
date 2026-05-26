from sortedcontainers import SortedDict

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.treemap = SortedDict()
        self.k_ = k
        self.size = 0
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if self.size < self.k_:
            self.increment(val)
            return self.treemap.keys()[0]
        min_ = self.treemap.keys()[0]
        if val < min_:
            return min_
        else:
            self.increment(val)
            self.decrement_min()
        return self.treemap.keys()[0]


    def increment(self, val: int):
        self.treemap[val] = self.treemap.get(val, 0) + 1
        self.size += 1
    
    def decrement_min(self):
        min_ = self.treemap.keys()[0]
        if self.treemap[min_] == 1:
            self.treemap.pop(min_)
        else:
            self.treemap[min_] = self.treemap[min_] - 1
        self.size -= 1
