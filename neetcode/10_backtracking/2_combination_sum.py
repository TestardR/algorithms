class Solution:
    def combinationSum(self, candidates, target: int):
        res = []
        
        subset = []

        def backtrack(i, total):
            if total == target:
                res.append(subset[:])
                return
            
            if i >= len(candidates) or total > target:
                return

            # decision to include candidates[i]
            subset.append(candidates[i])
            # add same candidate
            backtrack(i, total + candidates[i])
            
            # decision to include candidates[i]
            subset.pop()
            backtrack(i + 1, total)

        backtrack(0, 0)
        return res
    
print(Solution().combinationSum([2, 3, 6, 7], 7))