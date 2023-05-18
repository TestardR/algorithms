# Time complexity O(n * klogk)
""" 
def medianSlidingWindow(nums, k):
    n = len(nums)
    cur_arr = nums[:k-1]
    ans = []
    
    for i in range(k-1, n):
        if i > k - 1:
            cur_arr.pop(0)
            
            
        cur_arr.append(nums[i])
        
        sorted_arr = sorted(cur_arr)
        
        if k % 2:
            ans.append(sorted_arr[k//2])
        else:
            ans.append(sorted_arr[k//2] + sorted_arr[k//2-1] / 2)
            
        return ans
"""

import heapq
    
# Priority queue
class SlidingWindowMedian:
    def __init__(self,):
        self.maxHeap, self.minHeap, self.ans = [], [], []
    
    def insert(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
            
    def remove(self, heap, element):
        ind = heap.index(element) # find the element
        # mode the element to the end and delete it
        heap[ind] = heap[-1]
        del heap[-1]
        
        heapq.heapify(heap) # O(n)
        
        # if ind < len(heap): # O(log n)
        #     heapq._siftup(heap, ind)
        #     heapq._siftdown(heap, 0, ind)
            
    def rebalance(self):
        # either both the heaps will have equal number of elements or max-heap will have one
        # more element then the min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))   
    
    def get_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0)

        return -self.maxHeap[0] / 1.0     
        
    def find_sliding_window_median(self, nums, k):
        for i in range (len(nums)):
            self.insert(nums[i])
            self.rebalance()
            
            if i - k + 1 >= 0: # if we at least 'k' elements in the sliding window
                self.ans.append(self.get_median())
                
                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -elementToBeRemoved)
                else:
                    self.remove(self.minHeap, elementToBeRemoved)

                self.rebalance()
        
        return self.ans
        

def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 2)
    print("Sliding window medians are :", str(result))
    
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are :", str(result))
    
    
main()