class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        i = 0
        while i < 32:
            # print(f"n={n}")
            # print(f"ret={ret}")
            ret = ret << 1
            if n % 2 != 0:
                ret += 1
            n = n >> 1 
            i += 1
        return ret
        