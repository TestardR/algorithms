def find_missing_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
            
    
    missing_numbers = []
    
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)
            
    
    return missing_numbers
            
print(find_missing_numbers([2, 4, 1, 2]))