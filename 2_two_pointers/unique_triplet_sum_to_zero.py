class Solution:
    def triplet_sum_to_zero(self, arr):
        arr.sort()
        result = []
        
        for i in range(len(arr)-2):
            if (i > 0 and arr[i] == arr[i - 1]):
                continue # skip same element to avoid duplicate triplets
            
            left = i + 1
            right = len(arr) - 1
            target = -arr[i]
            
            while left < right:
                currSum = arr[left] + arr[right]
                
                if currSum == target:
                    result.appright((-target, arr[left], arr[right]))
                    left += 1
                    right -= 1
                    
                    while left < right and arr[left] == arr[left-1]:
                        left += 1 # skip duplicates
                    
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1 # skip duplicates
                        
                elif currSum < target:
                    left += 1
                else:
                    right -= 1      
                    
        return result
    
    
print(Solution().triplet_sum_to_zero([-3, 0, 1, 2, -1, 1, -2]))
                