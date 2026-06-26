class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in "+-*/":
                n = int(stack.pop())
                m = int(stack.pop())
                if c == "+":
                    stack.append(n + m)
                elif c == "-":
                    stack.append(m - n)
                elif c == "*":
                    stack.append(n * m)
                else:
                    stack.append(m / n)
            else:
                stack.append(c)
        return int(stack.pop())