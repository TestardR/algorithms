def find_subsets(nums):
    subsets = []    
    subsets.append([])
    for currentNumber in nums:
        for i in range(len(subsets)):
            set = list(subsets[i])
            set.append(currentNumber)
            subsets.append(set)
    
    return subsets

def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))

main()

