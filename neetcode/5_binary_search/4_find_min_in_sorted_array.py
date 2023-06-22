class Solution:
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1 
        res = float("inf")
        
        while start <= end :
            mid = (start + end ) // 2
            res = min(res, nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return res

print(Solution().findMin([2, 3, 4, 5, 1]))