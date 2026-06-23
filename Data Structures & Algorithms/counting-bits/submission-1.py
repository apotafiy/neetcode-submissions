class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        i = 0
        while i <= n:
            count = 0
            num = i
            while num > 0:
                count += num % 2
                num = num >> 1
            counts.append(count)
            i += 1
        return counts

        