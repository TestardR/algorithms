import heapq

# maxHeap [3, 1, 0] => in python [-3, -1, 0]
# minHeap [4, 6, 7]


class MedianFinder:
    def __init__(self):
        self.maxheap = []  # maxheap containing first half of numbers
        self.minheap = []  # minheap containing second half of numbers

    def addNum(self, num):
        if not self.maxheap or -self.maxheap[0] >= num:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        # either both the heaps will have equal number of elements or max-heap will have one
        # more element then the min-heap
        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        elif len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self):
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] / 2.0 + self.minheap[0] / 2.0)

        return -self.maxheap[0] / 1.0


def main():
    medianFinder = MedianFinder()
    medianFinder.addNum(3)
    medianFinder.addNum(1)
    print("The median is: " + str(medianFinder.findMedian()))
    medianFinder.addNum(5)
    print("The median is: " + str(medianFinder.findMedian()))
    medianFinder.addNum(4)
    print("The median is: " + str(medianFinder.findMedian()))

main()