class Solution():
    def sortedSquares(self, nums):
        result = [None for _ in range(len(nums))]
        leftIdx = 0
        rightIdx = len(nums) - 1

        while leftIdx <= rightIdx:
            if abs(nums[leftIdx]) < abs(nums[rightIdx]):
                result[rightIdx - leftIdx] = (nums[rightIdx]**2)
                rightIdx -= 1
            else:
                result[rightIdx - leftIdx] = (nums[leftIdx]**2)
                leftIdx += 1

        return result