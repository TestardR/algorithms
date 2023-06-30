class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()

        res = []
        subset = []

        def backtrack(pos, target):
            if target == 0:
                res.append(subset[:])
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                
                subset.append(candidates[i])
                backtrack(i + 1, target - candidates[i])
                subset.pop()
                
                prev = candidates[i]

        backtrack(0, target)
        return res
    
print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))