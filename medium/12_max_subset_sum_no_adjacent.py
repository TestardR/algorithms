# O(N) T | O(N)
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i -2] + array[i])
        
    return maxSums[-1]

# O(N) T | O(1) S
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    
    # second and first should be understood from the element array[i] distance (first = prev el, second = prev prev el)
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second, first = first, current
    
    return first


print(str(maxSubsetSumNoAdjacent([7, 10, 12, 7, 9, 14])))