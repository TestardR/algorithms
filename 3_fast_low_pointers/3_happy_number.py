class Solution:
    def happy_number(self, num):
        slow = num
        fast = num
        
        while True:
            slow = self.find_square_sum(slow)
            fast = self.find_square_sum(self.find_square_sum(fast))
            if slow == fast: 
                break
        
        return slow == 1
    
    def find_square_sum(self, num):
        sum = 0
        
        while num > 0:
            digit = num % 10
            sum += pow(digit, 2)
            num //= 10
            
        return sum
    
print(Solution().happy_number(12))