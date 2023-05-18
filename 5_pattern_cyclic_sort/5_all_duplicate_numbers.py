def find_all_dupicates(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else: 
            i += 1
            
    duplicate_nums = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicate_nums.append(nums[i])
            
    return duplicate_nums