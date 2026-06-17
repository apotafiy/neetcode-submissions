class Solution:
    def isHappy(self, n: int) -> bool:
        set_ = set()
        set_.add(n)
        while n != 1:
            s = str(n)
            squares = [int(c) ** 2 for c in list(s)]
            n = sum(squares)
            if n in set_:
                return False
            set_.add(n)
        return True