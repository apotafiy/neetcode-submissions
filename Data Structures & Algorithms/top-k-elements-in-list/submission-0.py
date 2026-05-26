class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        counts_sorted = sorted(counts.items(), key = lambda item: item[1], reverse = True)
        return list(map(lambda item: item[0], counts_sorted[0: k]))