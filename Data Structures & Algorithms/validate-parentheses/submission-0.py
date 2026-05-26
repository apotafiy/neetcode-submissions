class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {']': '[', ')': '(', '}': '{'}
        for char in s:
            if char in brackets.values():
                stack.append(char)
            else:
                if len(stack) == 0: return False
                top = stack[-1]
                if brackets.get(char) == top:
                    stack.pop()
                else: return False
        return len(stack) == 0