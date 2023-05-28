# list of numbers
# iterate multiple times over list, swap numbers if unsorted
# inner loop goes backward

# O(N^2) T | O(1) S
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j - 1, array)
            j -= 1
            
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]