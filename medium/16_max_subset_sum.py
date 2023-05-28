# [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
#  3, 8, -1, 1, 4,  2, 5, 9,16,18,  9,15,18,19, 14,18] 

# Algorithm
# maxEndingHere = max(maxEndHere + num, num)
# maxSoFar = max(maxSoFar, maxEndingHere)

# O(N) T | O(N) S

def kadanesAlgorithm(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    
    for num in array[1:]:
        maxEndingHere = max(maxEndingHere + num, num)
        maxSoFar = max(maxSoFar, maxEndingHere)
        
    return maxSoFar
        
print(str(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])))