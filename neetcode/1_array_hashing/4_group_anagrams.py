import collections

class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                # mapping letters to numbers
                # ord("a") - ord("a") = 0
                count[ord(c) - ord("a")] += 1
            
            # ex count = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
            #             a           e                                            t
            # list cannot be keys
            ans[tuple(count)].append(s)
        return ans.values()
    

print(Solution().groupAnagrams(["eat", "tea", "tan", "nat", "bat"]))

# T O(M*N)