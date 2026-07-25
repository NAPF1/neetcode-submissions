class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        pars = ""

        def recurse(openP, closeP):
            if openP == closeP == n:
                res.append("".join(stack))
                return

            if openP < n:
                stack.append("(")
                recurse(openP + 1, closeP)
                stack.pop()
            if closeP < openP:
                stack.append(")")
                recurse(openP, closeP + 1)
                stack.pop()

        recurse(0, 0)
        return res