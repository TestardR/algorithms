class Solution:
    def isValid(self, s):
        stack = []
        parenthesesMap = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char not in parenthesesMap:
                stack.append(char)
                continue
                
            if not stack or stack[-1] != parenthesesMap[char]:
                return False
            
            stack.pop()
            
        return not stack
