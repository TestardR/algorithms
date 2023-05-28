# O(N^2) T | O(N) S
def treeNumberSum(array, target):
    array.sort()
    triplets = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            currSum = array[i] + array[left] + array[right]
            if currSum > target:
                right -= 1
            elif currSum < target:
                left += 1
            else:
                triplets.append([array[left], array[right], array[i]])
                right -= 1 
                left += 1
                # increase both as only one with necessarily give a result > or < then target

    return triplets


print(str(treeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)))

# [12, 3, 1, 2, -6, 5, -8, 6]
# [-8, -6, 1, 2, 3, 5, 6, 12]
