import math


class Solution:
    def triplet_sum_close_to_target(self, arr, k):
        arr.sort()
        
        smallest_diff = math.inf
        
        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1
            
            while left < right:
                target_diff = k - arr[i] - arr[left] - arr[right]
                if target_diff == 0:
                    return k
                
                if abs(target_diff) < abs(smallest_diff):
                    smallest_diff = target_diff
                
                if target_diff > 0:
                    left += 1
                else:
                    right -= 1
                    
        return k - smallest_diff
        
        
print(Solution().triplet_sum_close_to_target([-2, 0, 1, 2], 2))