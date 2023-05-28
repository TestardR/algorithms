import math

# O(Nlog N) T due to sorting | O(1) S
def smallestDifference(array1, array2):
    array1.sort()
    array2.sort()
    idx1 = 0
    idx2 = 0
    smallestDifference = math.inf
    pair = []
    
    while idx1 < len(array1) and idx2 < len(array2):
        if abs(array1[idx1] - array2[idx2]) < smallestDifference:
            smallestDifference = abs(array1[idx1] - array2[idx2])
            pair = [array1[idx1], array2[idx2]]
    
        if array1[idx1] < array2[idx2]:
            idx1 += 1
        else:
            idx2 += 1
            
    return pair
       
print(str(smallestDifference([-1, 5, 10, 20 , 28, 3], [26, 134, 135, 15, 17])))
    