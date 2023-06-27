# Solution 1: sort input array
# Solution 2: use a max heap
# Solution 3: use quick select algorithm

# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                    
            # swap p value for pivot
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]
            
        return quickSelect(0, len(nums) - 1)
    
    
        