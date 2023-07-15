import collections

# O(NLogN) | O(N)
# class Solution:
#     def groupAnagrams(self, strs):
#         hashmap = {}
        
#         for s in strs:
#             word = "".join(sorted(s))
#             if word in hashmap:
#                 hashmap[word].append(s)
#             else:
#                 hashmap[word] = [s]
                
#         return hashmap.values()
        
            
class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
            
        return ans.values()