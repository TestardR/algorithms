# O(2)^t 2 decisions per node, (t)arget level

class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            
            cur.pop()
            
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res
    
print(Solution().combinationSum([2,3,6,7], 7))

### subsets
# [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [1, 2], [1, 3, 4], [1, 3], [1, 4], [1], [2, 3, 4], [2, 3], [2, 4], [2], [3, 4], [3], [4], []]
# class Solution:
#     def subsets(self, nums):
#         res = []
         
#         def dfs(i, subset):
#             if i == len(nums):
#                 res.append(subset[:])
#                 return
            
#             # decision to include nums[i]
#             subset.append(nums[i])
#             dfs(i + 1, subset)
#             # decision NOT to include nums[i]
#             subset.pop()
            
#             dfs(i + 1, subset)    
        
#         dfs(0, [])
#         return res        
    
    
# print(Solution().subsets([1, 2, 3, 4]))