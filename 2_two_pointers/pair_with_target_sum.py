class Solution:
    def pair_with_target_sum(self, arr, k):
        left = 0
        right = len(arr) - 1

        while left < right:
            currSum = arr[left] + arr[right]

            if currSum == k:
                return (arr[left], arr[right])

            if k > currSum:
                left += 1
            else:
                right -= 1
                
                
        return (-1, -1)

# The time complexity of the above algorithm will be O(N), where N is the total number of elements in the given array.
# Space complexity runs in constat space O(1)
