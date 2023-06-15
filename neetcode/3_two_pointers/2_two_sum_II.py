# sorted array as input
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIdx = 0
        rightIdx = len(numbers) - 1

        while leftIdx < rightIdx:
            currSum = numbers[leftIdx] + numbers[rightIdx]

            if target > currSum:
                leftIdx +=1
            elif target < currSum:
                rightIdx -= 1
            else:
                return [leftIdx + 1, rightIdx + 1]

        return [-1, -1]