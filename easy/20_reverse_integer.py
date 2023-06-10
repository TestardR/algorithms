class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            digit = x % 10
            reverse = reverse * 10 + digit
            x /= 10

        result = sign * reverse

        print(result)
        if result < -(2 ** 31) or result > (2 ** 31) -1:
            return 0

        return result