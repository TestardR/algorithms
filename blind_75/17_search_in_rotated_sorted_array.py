class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            # if left part is monotonically increasing, or the pivot point is on the right part
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # right sorted portion
            #if right part is monotonically increasing, or the pivot point is on the left part
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
