class Solution:
    def remove(self, arr):
        next_non_duplicate = 1
        for i in range(1, len(arr)):
            if arr[next_non_duplicate - 1] != arr[i]:
                arr[next_non_duplicate] = arr[i]
                next_non_duplicate += 1
                
                
        return next_non_duplicate
    
    
Solution().remove([2,3,3,3,6,6,9])