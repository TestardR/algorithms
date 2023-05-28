# [-1, -5, -10, -1100, -1100, -1101, -1102]
# O(N) T | O(1) S
# def isMonotonic(array):
#     if len(array) <= 2:
#         return True
    
#     direction = array[1] - array[0]
#     for i in range(2, len(array), direction):
#         if direction == 0:
#             direction = array[i] - array[i - 1]
#             continue
#         if breaksDirection(direction, array[i - 1], array[i]):
#             return False
    
#     return True


# def breaksDirection(direction, previousInt, currentInd):
#     difference = currentInd - previousInt
#     if direction > 0: # increment
#         return difference < 0 # decrement
#     return difference > 0 # decrement # increment

# O(N) T | O(1) S
def isMonotonic(array):
    isIncreasing = True # increment
    isDecreasing = True # decrement
    
    for i in range (1, len(array)):
        if array[i] < array[i -1]:
            isIncreasing = False
        if array[i] > array[i - 1]:
            isDecreasing = False
            
    return isIncreasing or isDecreasing


print(str(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102])))

