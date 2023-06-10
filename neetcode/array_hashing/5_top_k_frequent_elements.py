class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        # bucket sort: an array per index, we will store all elements occuring n times, in nth array
        freq = [[] for _ in range(len(nums))]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # loop in reverse order, from 0 until last index
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                

print(Solution().topKFrequent([1,1,1,2,2,3], 2))
               
