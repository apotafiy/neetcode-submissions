class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        end = len(s) - 1

        for i in range(0, int(len(s)/2)):
            if s[i] != s[end - i]:
                return False
        return True

        