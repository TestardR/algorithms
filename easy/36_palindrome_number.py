class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        inputNum = x
        revertedNum = 0
        while x > 0:
            revertedNum = revertedNum * 10 + x%10
            x = x//10 
            
        return inputNum == revertedNum