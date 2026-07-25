class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]

        for t in tokens:
            if t not in ops:
                stack.append(t)
            else:
                res = int(stack.pop())
                if t == "+":
                    res += int(stack.pop())
                elif t == "-":
                    res = int(stack.pop()) - res
                elif t == "*":
                    res *= int(stack.pop())
                elif t == "/":
                    res = int(stack.pop()) / res
                stack.append(res)
                print(res)
        return int(stack.pop())

        # Identify number or arith *
        # Push numbers into stack until arith
        # Add numbers to string as enter stack
        # When arith, add between numbers
        # Pop the numbers preceeding.
        # When stack is empty, return string
        