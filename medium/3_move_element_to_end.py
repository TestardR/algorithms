# O(N) T | O(1) S
def moveElementToTheEnd(array, target):
    left = 0 
    right = len(array) - 1
    
    while left < right:
        while array[right] == target:
            right -= 1
        
        if array[left] == target:
            array[left], array[right] = array[right], array[left]

        left += 1
        
    return array
            
            
print(str(moveElementToTheEnd([2, 1, 2, 2, 2, 3, 4, 2], 2)))