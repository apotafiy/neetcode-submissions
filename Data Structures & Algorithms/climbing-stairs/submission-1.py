class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        memo = [0, 1, 2]
        for i in range(3, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        print(memo)
        return memo[n]
        