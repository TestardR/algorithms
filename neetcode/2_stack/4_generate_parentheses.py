class Solution:
    def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            # add open parenthesis if open < n
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            # add closing parenthesis if closed < open
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()  

        backtrack(0, 0)
        return res
    
print(Solution().generateParenthesis(3))