class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = False
        for i in range(len(digits) - 1, -1, -1):
            n = digits[i]
            m = n + 1
            if m == 10:
                remainder = True
                digits[i] = 0
            else:
                remainder = False
                digits[i] = m
                break
        if remainder:
            digits = [1] + digits
        return digits

