# class Solution:
#     def topKFrequent(self, nums, k):
#         count = {}
#         freq = [[] for _ in range(len(nums) + 1)]
        
#         for n in nums: #O(N)
#             count[n] = count.get(n, 0) + 1
            
             
#         for n, c in count.items(): # O(N)
#             freq[c].append(n)
            
#         res = []
#         for i in range(len(freq) -1, -1, -1): #O(N)
#             for n in freq[i]: 
#                 res.append(n)
#                 if len(res) == k:
#                     return res
       
import heapq
         
class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = []
        
        for n in nums: # O(N)
            count[n] = count.get(n, 0) + 1
            
        for n, c in count.items(): #O(N)
            freq.append((-c, n))
            
        heapq.heapify(freq) #O(N)
        res = []
        for _ in range(k): #O(K) => #O(KLogN)
            c, n = heapq.heappop(freq) #O(LogN)
            res.append(n)
            
        #O(N + KLogN)
        
        return res
            
        
        
print(Solution().topKFrequent([1,1,1,2,2,3], 2))