class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        chars = [str(n) for n in list(digits)]
        s = "".join(chars)
        num = int(s)
        num += 1
        s = str(num)
        digits = [int(c) for c in list(s)]
        return digits
        