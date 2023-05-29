class MinHeap:
    def __init__(self, array):
        self.heap = self.buidHeap(array)
        
    def buildHeap(self, array):
        # - 2 because siftUp does -1 :: not super clear
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx)):
            self.siftDown(currentIdx, len(array) - 1, array)
            
        return array
    
    # get child index of current node
    # as long as childr index <= endIdx
    # compare value with second child
    # if one of those is out of order with currentIdx
    # swap 
    # reset currentIdx and childOneIdx
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx % 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx    
            else:
                idxToSwap = childOneIdx
            
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break
                
    # get parent index of current node
    # swap them if out of order
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
                
    def peek(self):
        return self.heap[0]
    
    # swap root with last value 
    # pop last value 
    # sift down root value
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        # start index to last index
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove
    
    # add value add the end of the heap
    def insert(self, value):
        self.heap.append(value)
        # index of the current node
        self.siftUp(len(self.heap) - 1, self.heap)
    
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
        