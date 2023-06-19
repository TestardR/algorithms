# O(N) T | O(1) S
def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else: 
            return [row, col]
        
    
    return [-1, -1]

# O(logN) | O(1) S
def searchMatrix(matrix, target): 
    topR = 0
    botR = len(matrix) - 1
    while topR <= botR:
        row = (topR - botR) // 2
        if target > matrix[row][-1]:
            topR = row + 1
        elif target < matrix[row][0]:
            botR = row - 1
        else: 
            break
        
    if not (topR <= botR):
        return False
    
    row = (topR + botR) // 2
    leftIdx = 0
    rightIdx = len(matrix[0]) - 1
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        if target > matrix[row][midIdx]:
            leftIdx = midIdx + 1
        elif target < matrix[row][midIdx]:
            rightIdx = midIdx - 1
        else:
            return True
        
    return False
        