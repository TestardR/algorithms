class Solution:
    def square_sorted_array(self, arr):
        highest_square_index = len(arr) - 1
        left = 0
        right = len(arr) - 1
        squares = [None for _ in arr]

        while left <= right:
            leftSq = pow(arr[left], 2)
            rightSq = pow(arr[right], 2)

            if leftSq > rightSq:
                squares[highest_square_index] = leftSq
                left += 1
            else:
                squares[highest_square_index] = rightSq
                right -= 1
                
            highest_square_index -= 1

        return squares


print(Solution().square_sorted_array([-2, -1, 0, 2, 3]))
