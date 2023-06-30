class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        
        subset = []

        def backtrack(i):
            if i == len(nums):
                res.append(subset[:])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            
            # decision NOT to include nums[i]
            subset.pop()
            
            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                
            backtrack(i + 1)

        backtrack(0)
        return res
    
print(Solution().subsetsWithDup([1, 2, 2, 4]))