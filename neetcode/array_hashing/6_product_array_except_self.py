# T O(N²) | S O(N)
# class Solution:
#     def productExceptSelf(self, nums):
#         res = [1] * len(nums)
        
#         for i in range(len(nums)):
#             pro = 1
            
#             for j in range(len(nums)):
#                 if i == j: continue
#                 pro *= nums[j]
                
#             res[i] = pro
            
#         return res

# T O(N) | S O(N)
# class Solution:
#     def productExceptSelf(self, nums):
#         res = [1] * len(nums)
        
#         pro = 1
#         for num in nums:
#             pro *= num
            
#         for i in range(len(nums)):
#             res[i] = pro // nums[i]
            
#         return res


# T O(N) | S O(N)
# class Solution:
#     def productExceptSelf(self, nums):
#         prefix = [1] * len(nums)
#         postfix = [1] * len(nums)
#         res = [1] * len(nums)
        
#         # store the product upto i-1 index
#         for i in range(1, len(nums)):
#             prefix[i] = prefix[i-1] * nums[i-1]
        
#         # store the product upto i+1 index
#         for i in range(len(nums) -2, -1, -1):
#             postfix[i] = postfix[i+1] * nums[i+1]
        
#         for i in range(len(nums)):
#             res[i] = prefix[i] * postfix[i]
            
#         return res
        
class Solution: 
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
    
    
print(Solution().productExceptSelf([1,2,3,4]))