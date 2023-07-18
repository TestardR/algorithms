class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1, 1

        for _ in range(n -1):
            tmp = n1
            n1 = n1 + n2
            n2 = tmp

        return n1

# T O(n)
# S O(1)