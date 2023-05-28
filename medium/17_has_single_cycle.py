# O(N) T | O(1) S
def hasSingleCycle(array):
    numElementsVisited = 0
    currentIdx = 0
    
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currentIdx == 0:
            return False
        numElementsVisited += 1
        currentIdx = getNextIds(currentIdx, array)
        
    return currentIdx == 0

def getNextIds(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array) # -1 (moving backward) is the same as -1 + len(array) (moving forward)
    
    