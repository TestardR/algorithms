#  1 
#+ 1 
# 10

# 11
#+ 1
# 100    

# 11
#+11
#110

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
                    # converts to int 
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2) # if total = 1: 1, 2: 0, 3: 1, also this is binary (aka base 2) so we mod 2
            res = char + res
            carry = total // 2 # if total = 2: 1, 3: 1, 1: 0

        if carry:
            res = "1" + res

        return res