# list of numbers 
# iterate over list, find smallest number
# swap smallest with first element of unsorted sublist

# O(N^2) | O(1)
def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array
        
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    
print(str(selectionSort([5, 4, 3, 2, 1])))