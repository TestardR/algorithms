class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case if len(nums) == 0
        # wihtout 0
        # without len(nums) - 1
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))   

    def helper(self, nums):
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
            
        return rob2 # by the end rob2 will be the last value (max we can rob)
# T O(n)
# S O(1)