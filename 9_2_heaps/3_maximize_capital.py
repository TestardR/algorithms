import heapq

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    minHeap = [] # K capital
    maxHeap = [] # P profit
    
    for i in range(len(profits)):
        heapq.heappush(minHeap, (capital[i], i))
        
    availableCapital = initialCapital
    for _ in range(numberOfProjects):
        while minHeap and minHeap[0][0] <= availableCapital:
            capital, i = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, (-profits[i], i))
            
        if not maxHeap:
            break
        
        availableCapital += -heapq.heappop(maxHeap)[0]
        
    return availableCapital
        
def main():
    print("Maximum capital: " + str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " + str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))
    
main()