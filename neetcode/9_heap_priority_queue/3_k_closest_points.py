import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            pts.append([dist, x, y])
            
        res = []
        heapq.heapify(pts)
        for _ in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
            
        return res