def find_subsets(nums):
    list.sort(nums)
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        if i > 0 and nums[i] == nums[i -1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex+1):
            set = list(subsets[j])
            set.append(nums[i])
            subsets.append(set)        
    return subsets

def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))

main()

