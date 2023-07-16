# class Solution:
#     def findMin(self, nums):
#         # set left and right bounds
#         left = 0
#         right = len(nums) - 1 
                
#         # left and right both converge to the minimum index;
#         # DO NOT use left <= right because that would loop forever
#         while left < right:
#             # find the middle value between the left and right bounds (their average);
#             mid = (left + right) // 2                        
#             if nums[mid] > nums[right]:
#                 # we KNOW the pivot must be to the right of the middle:
#                 # if nums[mid] > nums[right], we KNOW that the
#                 # pivot/minimum value must have occurred somewhere to the right
#                 # of mid, which is why the values wrapped around and became smaller.

#                 # example:  [3,4,5,6,7,8,9,1,2] 
#                 # in the first iteration, when we start with mid index = 4, right index = 9.
#                 # if nums[mid] > nums[right], we know that at some point to the right of mid,
#                 # the pivot must have occurred, which is why the values wrapped around
#                 # so that nums[right] is less then nums[mid]
#                 left = mid + 1

#             else:
#                 # here, nums[mid] <= nums[right]:
#                 # we KNOW the pivot must be at mid or to the left of mid:
#                 # if nums[mid] <= nums[right], we KNOW that the pivot was not encountered
#                 # to the right of middle, because that means the values would wrap around
#                 # and become smaller (which is caught in the above if statement).
#                 # this leaves the possible pivot point to be at index <= mid.
                            
#                 # example: [8,9,1,2,3,4,5,6,7]
#                 # in the first iteration, when we start with mid index = 4, right index = 9.
#                 # if nums[mid] <= nums[right], we know the numbers continued increasing to
#                 # the right of mid, so they never reached the pivot and wrapped around.
#                 # therefore, we know the pivot must be at index <= mid.

#                 # we know that nums[mid] <= nums[right].
#                 # therefore, we know it is possible for the mid index to store a smaller
#                 # value than at least one other index in the list (at right), so we do
#                 # not discard it by doing right = mid - 1. it still might have the minimum value.
#                 right = mid
                
#         # at this point, left and right converge to a single index (for minimum value) since
#         # our if/else forces the bounds of left/right to shrink each iteration:

#         # so we shrink the left/right bounds to one value,
#         # without ever disqualifying a possible minimum

#         return nums[left]

class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # min/pivot in the right
            if nums[mid] > nums[right]:
                left = mid + 1
            # min/pivot in the left
            else:
                right = mid
                
        return nums[left] 
            
    
print(Solution().findMin([11,13,15,17]))
