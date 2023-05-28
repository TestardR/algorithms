import pprint

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
                
        else:
            if self.right is None:
                self.right = BST(value)
            else: 
                self.right.insert(value)    
            

# O(Nlog(N)) T | O(N) S
def minHeightBST(array):
    return constuctMinHeightBST(array, None, 0, len(array) -1)
    
def constuctMinHeightBST(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return
    
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]
    
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
        
    constuctMinHeightBST(array, bst, startIdx, midIdx - 1)
    constuctMinHeightBST(array, bst, midIdx + 1, endIdx)
    
    return bst

# O(N) T | O(N) S
def minHeightBST(array):
    return constuctMinHeightBST(array, None, 0, len(array) -1)
    
def constuctMinHeightBST(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    
    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[startIdx])
    bst.left = constuctMinHeightBST(array, startIdx, midIdx - 1)
    bst.right = constuctMinHeightBST(array, midIdx + 1, endIdx)     
    
    return bst
    
print(minHeightBST([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    
