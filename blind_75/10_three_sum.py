class Solution:
    def threeSum(self, nums):
        nums.sort()
        triplets = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if currSum > 0:
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    
        return triplets
                
print(Solution().threeSum([-1,0,1,2,-1,-4]))