class MinMaxStack: 
    def __init__(self):
        self.minMaxStack = []
        self.stack = []
        
    # O(1) T | O(1) S
    def peek(self):
        return self.stack[len(self.stack) -1]
    
    # O(1) T | O(1) S
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()
    
    # O(1) T | O(1) S
    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) -1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = min(lastMinMax["min"], number)
            
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)
        
    # O(1) T | O(1) S
    def getMin(self):
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) -1]
            return lastMinMax["min"]
    
    # O(1) T | O(1) S
    def getMax(self):
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) -1]
            return lastMinMax["max"]