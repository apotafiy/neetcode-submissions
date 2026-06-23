class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]       
        if n == 1:
            return [0, 1]
        memo = [0, 1]
        subset = 0
        limit = 2
        for i in range(2, n + 1):
            memo.append(1 + memo[subset])
            subset += 1
            if subset == limit:
                subset = 0
                limit *= 2
        return memo