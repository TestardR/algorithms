class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":            
            return 0     

        dp = [0] * (len(s) + 1) # we want to account for number 0
        # we want to return the number of ways to decode string of the length s

        # dp will store number of ways to decode a string a of length x
        dp[0] = 1 
        dp[1] = 1
        
        # we want to include s length
        for i in range(2, len(s) + 1):
            # current digit
            if 1 <= int(s[i-1]) <= 9:
                dp[i] += dp[i - 1]
            
            # current digit and previous digit
            if 10 <= int(s[i-2] + s[i-1]) <= 26:
                dp[i] += dp[i - 2] 

        return dp[-1]