class Solution:
    def triplet_with_smaller_sum(self, arr, k):
        arr.sort()
        count = 0

        for i in range(len(arr)-2):
            left = i + 1
            right = len(arr) - 1
            target = k - arr[i]

            while left < right:
                if arr[left] + arr[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count


print(Solution().triplet_with_smaller_sum([-1, 0, 2, 3], 3))
